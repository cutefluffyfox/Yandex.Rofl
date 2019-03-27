# -*- coding: utf-8 -*-
from pandas import read_csv
from pymorphy2 import MorphAnalyzer
import string
from nltk import word_tokenize
from nltk.corpus import stopwords

df = read_csv("clear_text.csv")


def tokenize_me(file_text):
    tokens = word_tokenize(file_text.lower())

    def delete_bad(data: list):
        i = 0
        morph = MorphAnalyzer()
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
        alp = 'йцукенгшщзхъэждлорпавыфячсмитьбюё1234567890' + string.ascii_letters
        while i < len(data):
            if data[i] in stop_words:
                data.pop(i)
                continue
            for letter in data[i]:
                if letter not in alp:
                    data.pop(i)
                    break
            else:
                data[i] = morph.parse(data[i])[0].normal_form
                i += 1

    delete_bad(tokens)
    return " ".join(tokens)


check = df['Подробное описание'].apply(tokenize_me)

df['clear_text'] = check
df.to_csv("clear_text1.csv", encoding='utf-8')
