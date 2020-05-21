# ed4nlp is simple package that helps you to find ngram counts
## USAGE
### pip install eda4nlp

### from eda4nlp.utils import ngram

## ngram takes 5 arguemnts
#### ngram(corpus,ngram,stop_words,plot,topk)
#### corpus--> pass the pandas columns
#### ngram--> 1 if unigram, 2 if bigram , 3 if trigram
#### stop_words--> default is None. To use stop_words pass 'english'
#### plot=True, to plot the ngram vs count frequency distribution . defalut=False
#### topk to visual topk ngram counts in the plot
#### returns list with ngram and counts

### please refer Tutorial.ipynb file.
