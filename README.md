# NLP
In this section, learn how to apply Natrual language processing.
Files are:
- [Twitter_Extract.py]('https://github.com/parvanesh/NLP/blob/master/twitter_extract.py'):
Here, using Twitter API, we can extract the latest tweets using specif search term (in this example, Covid), and save the result in a csv file.
- [Word_cloud.py]('https://github.com/parvanesh/NLP/blob/master/Word_cloud.py'): In this file, we read the extracted tweets in previous step, to create a cloud of words. 
before creating the word cloud, it is needed to remove remove stopwords.
- [Word_frequency.py]('https://github.com/parvanesh/NLP/blob/master/Word_frequency.py'): In this file, display word frequency from extracted tweets. As a preprocessing process, these steps have been done:
removing stopwords, remove punctuations and word stemming. </br>
The main used package is NLTK.  