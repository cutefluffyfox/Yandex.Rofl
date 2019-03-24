# -*- coding: utf-8 -*-
from pandas import read_excel
from pymorphy2 import MorphAnalyzer
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from os import getcwd, path
df = read_excel(path.join(path.dirname(getcwd()), "ДТК Заявки_final.xlsx"))


def tokenize_me(file_text):
    # separate words + lower
    tokens = word_tokenize(file_text.lower())
    # let's delete punctuation symbols

    def delete_bad(data: list):
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на',
                           "_________________________________________________", "``", "-", "«", "»", "''", "–", "--",
                           "________________________________"])
        morph = MorphAnalyzer()
        i = 0
        while i < len(data):
            data[i] = data[i].lower()
            if data[i] in stop_words or data[i] in string.punctuation:
                data.pop(i)
            else:
                data[i] = morph.parse(data[i])[0].normal_form
                i += 1

    delete_bad(tokens)
    return tokens


length = len(df["Подробное описание"])
this = 0
for text in df["Подробное описание"]:
    a = tokenize_me(text)
    this += 1
    print(this / length * 100, this, a, sep="           ")
