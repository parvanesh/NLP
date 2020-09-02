import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
#Open csv file
all_tweets = pd.read_csv('tweets2.csv')
all_tweets['text'].head()

#Concat all tweets & lower then
all_text = "".join(all_tweets.text)
all_text = all_text.lower()

#Call stopwords & aggregate extra stop words
stopwords = STOPWORDS.copy()
stopwords.update(['https','amp'])

#Create Wordcloud
wordcloud = WordCloud(stopwords = stopwords, width = 1200, height = 600).generate(all_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()