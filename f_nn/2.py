import pandas as pd              # A beautiful library to help us work with data as tables
import numpy as np               # So we can use number matrices. Both pandas and TensorFlow need it.
import matplotlib.pyplot as plt  # Visualize the things
import tensorflow as tf          # Fire from the gods

dataframe = pd.read_csv("data.csv") # Let's have Pandas load our dataset as a dataframe
dataframe = dataframe.drop(["index", "price", "sq_price"], axis=1) # Remove columns we don't care about
dataframe = dataframe[0:10] # We'll only use the first 10 rows of the dataset in this example

dataframe.loc[:, ("y1")] = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1] # This is our friend's list of which houses she liked # 1 = good, 0 = bad
dataframe.loc[:, ("y2")] = dataframe["y1"]==0   # y2 is the negation of y1
dataframe.loc[:, ("y2")] = dataframe["y2"].astype(int)    # Turn TRUE/FALSE values into 1/0

# y2 means we don't like a house
# (Yes, it's redundant. But learning to do it this way opens the door to Multiclass classification)

inputX = dataframe.loc[:, ['area', 'bathrooms']].as_matrix()
inputY = dataframe.loc[:, ["y1", "y2"]].as_matrix()

print(inputX)