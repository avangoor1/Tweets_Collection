# This file will be used to create the linear regression model to label each tweet as merit or luck. It takes in
# a regression file that should have each tweet labelled as either 1 for merit or 0 for luck. 

# Imports
import spacy
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
import os

#Load a large language model and assign it to the variable 'nlp_lg'
nlp_lg = spacy.load('en_core_web_lg')

# Lists to hold X (embeddings) and Y (relevancy values)
X = []
Y = []

class EmbeddedTweet:
    def __init__(self, tweet_id: int, text: str, embedding: np.array, relevancy: int):
        self.tweet_id = tweet_id
        self.text = text
        self.embedding = embedding
        self.relevancy = relevancy
    
    def print(self):
        print("The object's embedding is" + str(self.embedding) + "\n")


# Open the CSV file in read mode
with open('', mode='r', newline='', encoding='utf-8') as file: # add the regression file that you created where you labelled each tweet as either merit or luck
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Loop through each line in the CSV file
    for row in csv_reader:
        tweet_id = int(row[0])
        author_id = int(row[1])
        date_published = row[2]
        text = row[3]  
        relevancy = int(row[4])  
        embedding = nlp_lg(text)
        object = EmbeddedTweet(tweet_id, text, embedding.vector, relevancy) 
        # print(object.print())
        # Append embedding and relevancy to respective lists
        X.append(embedding.vector)
        Y.append(relevancy)

# Convert X and Y to numpy arrays
X = np.array(X)
Y = np.array(Y)

# Initialize the LinearRegression model
model = LinearRegression()

# Fit the model to your data
model.fit(X, Y)

# Print the coefficients to see what the model has learned
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

output_file = "" # the file that you want to output the labelled tweets to
input_file = "" # the file you want to pass the filter through

with open(output_file, mode='w', newline='', encoding='utf-8') as output:
    csv_writer = csv.writer(output) 
    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Loop through each line in the CSV file
        for row in csv_reader:
            tweet_id = int(row[0]) 
            author_id = int(row[1])
            date_published = row[2]
            text = row[3]  
            embedding = nlp_lg(text).vector
            embedding = embedding.reshape(1, -1)
            predicted_relevancy = model.predict(embedding)
            predicted_class = 1 if predicted_relevancy[0] > 0.5 else 0
            print(predicted_class)
            if predicted_class == 1:
                csv_writer.writerow([tweet_id, author_id, date_published, f"{text}", 1]) # add a "1" at the end to showcase the tweet as pro-merit
            else:
                csv_writer.writerow([tweet_id, author_id, date_published, f"{text}", 0]) # add a "0" at the end to showcase the tweet as pro-luck



output.close()