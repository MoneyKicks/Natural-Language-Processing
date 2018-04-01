
# coding: utf-8

# In[31]:


#Lemmatizing is actually a better technique than stemming as it gives the actual meaning of the word which in a way
#is quite closer to it's sense in which it is being used in the sentence.

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("fly",pos="v"))
print(lemmatizer.lemmatize("drive",pos="a"))
print(lemmatizer.lemmatize("running",pos="v"))
print(lemmatizer.lemmatize("playful",pos="n"))
print(lemmatizer.lemmatize("playing",pos="v"))
print(lemmatizer.lemmatize("skating",pos="a"))

