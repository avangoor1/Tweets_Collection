This repository will give you access to query for more tweets. You can query for tweets using specific hashtags or a combination of phrases. It will also give you the access to
filter the tweets based on relevancy. Then, you can also use a filter to label the tweets as either merit or luck. Finally, you would have a high quality training data set.


Step 0: Set up a virtual environment. This ensures that all required libraries and their specific versions are installed in an isolated space, preventing conflicts with other projects on your system. You can use this command in the terminal to create the virtual environemnt: "python3 -m venv venv" and then activate it using "source venv/bin/activate".

Step 1: There is a file called "requirements.txt". This has all the libraries and thier specific versions you need to succesfully run the files in the repository. You can use this command to download the libraries: pip install -r requirements.txt.

Now, your system is ready to collect more tweets.

Step 2: Under the "Get Tweets Programs" folder, you can use either the 'getTweetsByHashtag.py' or 'getTweetsKeyWords.py' programs to collect the tweets. One program is specific to collecting tweets based on a hashtag and the other is for collecting based on one of the four queries below:

    #query = "(reaganomics OR tax the rich OR tax cut OR trickle down) OR (lobbying OR lobbyist) OR (outsourced labor OR at will employment)"
    #query = "trans rights OR my body my choice OR free palestine OR dialectic OR dialectical materialism OR workers rights OR oligarch OR oligarchy"
    #query = "drain the swamp OR deep state OR government spending OR corrupt democrat OR RINO OR Obamacare OR border crisis"
    #query = "(hustle OR grindset) OR (portfolio OR shares OR self-made) OR (affirmative action OR DEI OR radical OR Soros)"

Step 3: Not every tweet you get the running the programs above will be relevant to the topic of success in the workplace setting. Therefore, you must run the tweets through two filters. First, you must filter the tweets through the relevancy filter. Label 10% of the tweets you received after running Step 2 as either 1 for relevant and 0 for irrelevant.

Step 4: Use the labeled tweets to train a linear regression model capable of classifying new tweets as either relevant or irrelevant. The relevant tweets will be put into a new file.

Step 5: Now, you need to label the relevant tweets as either merit or luck. Therefore, you need to create another filter that would do this. Label 10% of the tweets you received after running Step 4 as either 1 for merit and 0 for luck.

Step 6: Run the rest of the 90% of tweets through the filter in Step 5 to label the tweets as either merit or luck. Now, you have high quality tweets that can be trained on. Set this set of trained tweets aside as you use them to tarin your neural network.


