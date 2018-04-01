
# coding: utf-8

# In[9]:


import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
sample='Ram is a good boy. He lives in Delhi. He goes to school daily. He studies in Bal Bharti Public School located in Vasant Kunj'
sentences=sent_tokenize(sample)
for sentence in sentences:
    tagged=nltk.pos_tag(word_tokenize(sentence))
    namedEnt=nltk.ne_chunk(tagged,binary=True)
    namedEnt.draw()

