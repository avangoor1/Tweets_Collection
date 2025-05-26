# Tweet Classification Project

## Overview
This repository allows you to query and collect tweets related to public discourse around success, using specific hashtags or keyword combinations. You can:

- Query tweets using hashtags or phrases.
- Filter tweets for **relevancy**.
- Further label relevant tweets as either **merit** or **luck**.
- Generate a **high-quality training dataset** to develop a neural network.

---

## Setup Instructions

### Step 0: Set Up a Virtual Environment
A virtual environment ensures that all required libraries (and their versions) are installed in an isolated workspace.

Run the following commands in your terminal:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 1: Install Dependencies
The `requirements.txt` file contains all the necessary libraries.

Install them using:

```bash
pip install -r requirements.txt
```

Your system is now ready to collect and process tweets.

---

## Tweet Collection & Processing Pipeline

### Step 2: Collect Tweets
Navigate to the `Get Tweets Programs` folder. You can choose between:

- `getTweetsByHashtag.py` — to collect tweets using a specific hashtag.
- `getTweetsKeyWords.py` — to collect tweets using one of the following predefined queries:

```python
query1 = "(reaganomics OR tax the rich OR tax cut OR trickle down) OR (lobbying OR lobbyist) OR (outsourced labor OR at will employment)"
query2 = "trans rights OR my body my choice OR free palestine OR dialectic OR dialectical materialism OR workers rights OR oligarch OR oligarchy"
query3 = "drain the swamp OR deep state OR government spending OR corrupt democrat OR RINO OR Obamacare OR border crisis"
query4 = "(hustle OR grindset) OR (portfolio OR shares OR self-made) OR (affirmative action OR DEI OR radical OR Soros)"
```

---

### Step 3: Relevancy Filtering
Not all collected tweets will be relevant to the topic of **success in the workplace**. To filter them:

1. Manually label 10% of the tweets as:
   - `1` = Relevant
   - `0` = Irrelevant
  
Examples of Tweet Labeling  
Below are a few sample tweets and how they might be labeled:
     
| Tweet ID            | Tweet Text                                                                                                              | Label |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----- |
| 1866268380757471686 | *"A quick-fix way for Rachel Reeves to tax the wealthy #TaxtheRich"*                                                    | `0`   |
| 1866259279608733754 | *"As I've said many times, our civilization today is BUILT to funnel wealth upwards, and has for decades now.  Which is why we have so many billionaires, and soon we'll have TRILLIONAIRES.  The imbalance is staggering AND unsustainable.  #TaxTheRich to save our world. It's VITAL. https://t.co/GMmHzkOBt9 https://t.co/Uwefjc2jW8"* | `1`   |
| 1866466904258261357 | *"#TaxTheRich #ZeitFuerGruen  #Habeck4Kanzler   THIS 👇 https://t.co/c0dtpu0XQa"*                                       | `0`   |
| 1866160613468111045 | *"Let's tax the rich - that's how you can actually ""make America great again.""   The massive inequality we see in this country began to explode over decades of handing out tax giveaways to the wealthiest in our society.  #TaxTheRich https://t.co/NLqxIRqlZO"*                              | `1`   |


2. Use this labeled subset to train a **relevancy classifier** such as a linear regression model. You can explore the classifier.py program. The program takes in two csv files. The first csv file contains your labelled relevancy tweets. The second csv file contains the tweets that you want the regression model to filter. All these files are commented out in the code for you.

3. Apply the trained classifier to the rest of the tweets. Save only the **relevant tweets** for the next step.

---

### Step 4: Merit vs. Luck Classification
1. Manually label 10% of the **relevant** tweets as:
   - `1` = Merit
   - `0` = Luck

2. Train a second classifier using this labeled data.

3. Run the remaining 90% of relevant tweets through the trained model to label them as either **merit** or **luck**.

---

## Final Output
You now have a **high-quality, labeled dataset** of tweets relevant to success in the workplace, classified by perceived cause (merit or luck). This dataset can be used to train your neural network or for other analytical purposes.

---

## Suggestions for Improvement
- Include example inputs/outputs for your scripts.
- Add usage instructions for each Python file (`getTweetsByHashtag.py`, etc.).
- Include error handling tips or common issues (e.g., Twitter API limits, authentication setup).
