import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re

#Read all tweets
all_tweets = pd.read_csv('tweets2.csv')
all_tweets['text'].head()

#Concat all tweets & lower then
all_text = "".join(all_tweets.text)
all_text = all_text.lower()

# Add stopword
eng_Stopwords = stopwords.words('english')
eng_Stopwords.extend(['https','amp'])

#Clear stopwords & punctuations

cleaned = re.sub(r'[^(a-zA-Z)\s]','', all_text)
word_tokens = word_tokenize(cleaned)
filtered_Sentence = [w for w in word_tokens if w not in eng_Stopwords]
filtered_Sentence2 = [w for w in filtered_Sentence if w not in string.punctuation]

print(len(cleaned), len(filtered_Sentence), len(filtered_Sentence2))

#Calculate frequency dsitribution & create chart
res_freq = FreqDist(cleaned)
res_freq.plot(30, cumulative = False)

#Apply stemming
ps = PorterStemmer()
stemmed_Sent = [ps.stem(w) for w in cleaned ]

#Calculate frequency dsitribution & create chart
freqDist = FreqDist(stemmed_Sent)
freqDist.plot(30, cumulative = False)