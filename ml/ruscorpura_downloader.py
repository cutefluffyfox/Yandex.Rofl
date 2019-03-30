from gensim.downloader import load as model_load
model = model_load("word2vec-ruscorpora-300")
model.save("russian_database")
