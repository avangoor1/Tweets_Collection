# This file will allow you to query for queries based one of the four queries.

import requests
import csv
import os

BEARER_TOKEN = '' # add the Bearer token from the X API

# Define headers for authorization
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# Function to search for tweets with specific keywords and date
def search_tweets(date, max_results=100, next_token=None):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    
    # Define time range for the specified date
    start_time = f"{date}T00:00:00Z"
    end_time = f"{date}T23:59:59Z"
    
    # Query params - use one of the four queries
    params = {
        'query': "(hustle OR grindset) OR (portfolio OR shares OR self-made) OR (affirmative action OR DEI OR radical OR Soros)",
        'max_results': max_results,
        'start_time': start_time,
        'end_time': end_time,
        'tweet.fields': 'created_at,author_id,text,public_metrics,referenced_tweets',
        'expansions': 'referenced_tweets.id',
    }
    
    # Include pagination token if provided
    if next_token:
        params['next_token'] = next_token
    
    response = requests.get(search_url, headers=HEADERS, params=params)
    if response.status_code == 200:
        tweets_data = response.json()
        tweets = tweets_data.get("data", [])
        includes = tweets_data.get("includes", {})
        
        # Check if full text is in the includes data
        for tweet in tweets:
            ref_id = tweet.get('referenced_tweets', [{}])[0].get('id')
            if ref_id:
                full_tweet = next((item for item in includes.get('tweets', []) if item['id'] == ref_id), {})
                tweet['text'] = full_tweet.get('text', tweet['text'])
        
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
def fetch_and_save_tweets(date, output_file):
    all_tweets = []
    next_token = None
    max_tweets = 100
    
    while len(all_tweets) < max_tweets:
        tweets, next_token = search_tweets(date, next_token=next_token)
        if not tweets:
            print("No more tweets found.")
            break
        
        tweets_to_add = tweets[:max_tweets - len(all_tweets)] 
        all_tweets.extend(tweets_to_add)
        save_tweets_to_csv(tweets_to_add, output_file)
        print(f"Fetched {len(tweets_to_add)} tweets, total: {len(all_tweets)}")
        
        if not next_token:
            print("No more pages to fetch.")
            break

# Example usage
if __name__ == "__main__":
    date = "2025-3-19" # add the specific you want to query from
    output_file = "get_tweets_output_query4.csv" # add the file that you want the save the tweets to
    
    fetch_and_save_tweets(date, output_file)
    print(f"All tweets have been saved to '{output_file}'.")
