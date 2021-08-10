import pandas as pd 
import re 
import emoji
import nltk
nltk.download('words')
words = set(nltk.corpus.words.words())

tweet = pd.read_csv('new_BillGates_tweets.csv')

def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
         if w.lower() in words or not w.isalpha())
    return tweet

tweet['text'] = tweet['text'].map(lambda x: cleaner(x))
tweet.to_csv('cleanedGates.csv') #specify location
