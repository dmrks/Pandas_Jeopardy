#1 Given
import pandas as pd
pd.set_option('display.max_colwidth', -1)

#2 Strip Whitepace // Load Data
jeopardy = pd.read_csv("jeopardy.csv")
print(jeopardy.columns)
print(jeopardy.head(10))
jeopardy.columns = jeopardy.columns.str.lstrip()
print(jeopardy.head(10))
print(jeopardy.columns)

#3 Search/Filter Function
def search(data,words):
  search = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data["Question"].apply(search)]

#4 Test Function
applied_filter = search(jeopardy,["King","England"])
print(applied_filter["Question"])

applied_filter = search(jeopardy,["Queen","England"])
print(applied_filter["Question"])

#4 Convert the " Value" column to floats
jeopardy["float_values"] = jeopardy.Value.apply(lambda x: float(x[1:].replace(",","")) if x != "None" else 0)

#4b What is the average value of questions that contain the word "King"? Answer: 670.8108108108108

applied_filter = search(jeopardy,["King"])
print(applied_filter["float_values"].mean())

#5 Write a function that returns the count of the unique answers to all of the questions in a dataset

def return_answer_counts(data):
  return jeopardy["Answer"].value_counts()

print(return_answer_counts(applied_filter))








