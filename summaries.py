import numpy as np
import pandas as pd
import re

def summaries(raw_text):
  from nltk.tokenize import sent_tokenize

  # Extract word vectors
  word_embeddings = {}
  f = open('glove/glove.6B.100d.txt', encoding='utf-8')
  for line in f:
      values = line.split()
      word = values[0]
      coefs = np.asarray(values[1:], dtype='float32')
      word_embeddings[word] = coefs
  f.close()

  # remove punctuations, numbers and special characters
  clean_sentences = re.sub(r'\[\d+\]*', "",raw_text)
  sentences = sent_tokenize(clean_sentences)
  clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
  # make alphabets lowercase
  clean_sentences = [n.lower() for n in clean_sentences]

  from nltk.corpus import stopwords
  stop_words = stopwords.words('english')

  # function to remove stopwords
  def remove_stopwords(sen):
      sen_new = " ".join([i for i in sen if i not in stop_words])
      return sen_new

  # remove stopwords from the sentences
  clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

  sentence_vectors = []
  for i in clean_sentences:
    if len(i) != 0:
      v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
    else:
      v = np.zeros((100,))
    sentence_vectors.append(v)

  # similarity matrix
  sim_mat = np.zeros([len(sentences), len(sentences)])

  from sklearn.metrics.pairwise import cosine_similarity

  for i in range(len(sentences)):
    for j in range(len(sentences)):
      if i != j:
        sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

  import networkx as nx

  nx_graph = nx.from_numpy_array(sim_mat)
  scores = nx.pagerank(nx_graph)

  ranked_sentences = sorted((s for i,s in enumerate(sentences)), reverse=True)

  # print the length of the ranked sentence
  length = len(ranked_sentences) // 3
  output = " ".join(ranked_sentences[:length])

  return output