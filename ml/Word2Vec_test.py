from pandas import read_excel, read_csv
from os import path
from gensim.models import Word2Vec
df = read_csv(path.join("F:\трэш дата", "clear_text1.csv"))
what = "clear_text"
df = df[df[what] == df[what]]

answ = read_csv(path.join("F:\трэш дата", "clear_text1.csv"))
# first = 1000
# other = 100 + first
answ_col = "Решение"
# answ_col = what
# answ_train, answ_test = answ[answ_col][:first], df[answ_col][first:other]
# train_data, test_data = df["clear_text"][:first], df["clear_text"][first:other]
train_data = df["clear_text"]
word2vec = Word2Vec([phrase.split() for phrase in train_data], min_count=3)
while True:
    try:
        print(word2vec.wv.most_similar(input()))
    except KeyError:
        print("Нет в словаре")
# print(test_data[1001])
# print("--------------------------------------------------")
# print(answ_test[1001])
