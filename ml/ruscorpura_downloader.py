from gensim.downloader import load as model_load
import nltk

nltk.download('punkt')
nltk.download('stopwords')
model = model_load("word2vec-ruscorpora-300")
model.save("russian_database")
