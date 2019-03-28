from sklearn.feature_extraction.text import CountVectorizer
from pandas import read_excel, read_csv
from os import path, getcwd
from sklearn.neighbors import KNeighborsClassifier

df = read_csv(path.join("E:\трэш дата", "clear_text.csv"))
df = df[df['clear_text'] == df['clear_text']]

what = "Подробное описание"
answ = read_excel(path.join("E:\трэш дата", "ДТК Заявки_final.xlsx"))
answ = answ[answ[what] == answ[what]]
# print(CountVectorizer().fit_transform(df["clear_text"]).shape)
first = 5000
other = 100 + first
train_data, test_data = df["clear_text"][:first], df["clear_text"][first:other]
cv = CountVectorizer()
a = KNeighborsClassifier()
train_x = cv.fit_transform(train_data)
a.fit(train_x, answ[what][:first])
test_x = cv.transform(test_data)
ind = first
# for an in a.predict(test_x):
#     print(df["Подробное описание"][ind], an, sep="\n----\n", end="\n====================================\n\n\n\n\n")
#     ind += 1
