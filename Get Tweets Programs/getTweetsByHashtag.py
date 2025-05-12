# This file will allow you to query for queries based on specific hashtags.

import requests
import csv
import os
from datetime import datetime, timedelta

BEARER_TOKEN = '' # add teh Bearer token to access the X API 

# Define headers for authorization
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# Function to search for tweets with hashtag and date
def search_tweets(hashtag, date, max_results=100, next_token=None):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    
    # Define time range for the specified date
    start_time = f"{date}T00:00:00Z"
    end_time = f"{date}T23:59:59Z"
    
    # Query params
    params = {
        'query': f"#{hashtag} lang:en -has:media -is:retweet", 
        'max_results': max_results,  
        'start_time': start_time,   
        'end_time': end_time,      
        'tweet.fields': 'created_at,author_id,text',  
    }
    
    # Include pagination token if provided
    if next_token:
        params['next_token'] = next_token
    
    response = requests.get(search_url, headers=HEADERS, params=params)
    if response.status_code == 200:
        tweets_data = response.json()
        tweets = tweets_data.get("data", [])
        next_token = tweets_data.get('meta', {}).get('next_token', None)
        return tweets, next_token
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return [], None

# Function to save tweets to a CSV file
def save_tweets_to_csv(tweets, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        # Write header only if file does not exist
        if not file_exists:
            writer.writerow(["Tweet ID", "Author ID", "Created At", "Text"])
        
        # Write each tweet's data
        for tweet in tweets:
            tweet_id = tweet['id']
            author_id = tweet['author_id']
            created_at = tweet['created_at']
            text = tweet['text'].replace("\n", " ").replace("\r", "")  
            writer.writerow([tweet_id, author_id, created_at, f"\"{text}\""])

# Main function to fetch and save tweets
def fetch_and_save_tweets(hashtag, date, output_file):
    all_tweets = []
    next_token = None
    while True:
        tweets, next_token = search_tweets(hashtag, date, next_token=next_token)
        if not tweets:
            print("No more tweets found.")
            break
        
        all_tweets.extend(tweets)
        save_tweets_to_csv(tweets, output_file)
        print(f"Fetched {len(tweets)} tweets, total: {len(all_tweets)}")
        
        if not next_token:
            print("No more pages to fetch.")
            break

# Example usage
if __name__ == "__main__":
    hashtag = "DOGE" # add the hashtag you want to query for
    date = "2025-2-25" # add specific date you want to pull from
    output_file = "get_tweets_output.csv" # add the file you want to put the tweets you want to place the tweets in
    
    print(f"Fetching tweets for #{hashtag} on {date}...")
    fetch_and_save_tweets(hashtag, date, output_file)
    print(f"All tweets have been saved to '{output_file}'.")