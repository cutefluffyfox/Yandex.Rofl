from pandas import read_csv
from nltk import word_tokenize
from os import path
from nltk.corpus import stopwords

df = read_csv(path.join('D:\трэш дата', "final_text.csv"))

a = read_csv(r'D:\трэш дата\языки\city.csv')
a1 = list(a['country_en'].apply(str))
a1.extend(list(a['region_en'].apply(str)))
a1.extend(list(a['city_en'].apply(str)))
a1.extend(list(a['country'].apply(str)))
a1.extend(list(a['region'].apply(str)))
a1.extend(list(a['city'].apply(str)))
a1.extend(['ул'])
a1 = list(map(str.lower, a1))
a1 = list(set(a1))


def tokenize_me(file_text):
    file_text = str(file_text)
    tokens = word_tokenize(file_text.lower())

    def delete_bad(data: list):
        i = 0
        while i < len(data):
            if data[i] in a1:
                if data[i] == 'ул' and i + 1 < len(data):
                    data.pop(i + 1)
                data.pop(i)
            else:
                i += 1

    delete_bad(tokens)
    return " ".join(tokens)


check = df['clear_text'].apply(tokenize_me)

df['clear_text'] = check
df.to_csv("final_text.csv", encoding='utf-8')