import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt


def ngram(corpus, ngram=1, stop_words=None, plot=False,topk=20):
    vec = CountVectorizer(stop_words=stop_words, ngram_range=(ngram, ngram)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    if plot == True:
        df1 = pd.DataFrame(words_freq, columns=['ngram', 'count'])
        df1.iloc[:topk, :].plot(x='ngram', y='count', kind='bar')
        plt.xlabel('ngram')
        plt.ylabel('count')
        plt.show()


    else:
        pass

    return words_freq