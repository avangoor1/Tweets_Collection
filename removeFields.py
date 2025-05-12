# This file is used to remove certain fields from a tweet. For example, each tweet has tweet_id, author_id, date_published, and the text
# if you only wanted certain fields like only the tweet content, then you can use this program to remove the other fields and put it into
# a new file.

import csv

def keep_last_two_fields(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # Check if there are at least two fields
            if len(row) >= 2:
                # Write only the last two fields to the output file
                writer.writerow([row[-2]])  # First and last fields

# Example usage
input_file = 'Transfer Learning Dataset/luck_greaterthan200.csv'  # Replace with your input CSV file name
output_file = 'Transfer Learning Dataset/luck_greaterthan200_removed.csv'  # Replace with your output CSV file name

keep_last_two_fields(input_file, output_file)
