from pandas import read_csv
from pymorphy2 import MorphAnalyzer
import string
from nltk import word_tokenize
from nltk.corpus import stopwords

city_csv = read_csv('csv/city.csv')
cities = list(city_csv['country_en'].apply(str))
cities.extend(list(city_csv['region_en'].apply(str)))
cities.extend(list(city_csv['city_en'].apply(str)))
cities.extend(list(city_csv['country'].apply(str)))
cities.extend(list(city_csv['region'].apply(str)))
cities.extend(list(city_csv['city'].apply(str)))
cities.extend(['ул'])
cities = list(set(map(str.lower, cities)))

names = list(read_csv('csv/surnames.csv')['Surname'].apply(str))
names.extend(list(read_csv('csv/rus_names.csv')['Name'].apply(str)))
names.extend(list(read_csv('csv/for_names.csv')['name'].apply(str)))
names = list(map(str.lower, names))


def tokenize_me(file_text):
    def delete(data: list):
        morph = MorphAnalyzer()
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
        alp = 'йцукенгшщзхъэждлорпавыфячсмитьбюё1234567890' + string.ascii_letters

        i = 0

        while i < len(data):
            if data[i] in cities or data[i] in names or data[i] in stop_words:
                if data[i] == 'ул' and i + 1 < len(data):
                    data.pop(i + 1)
                data.pop(i)
                continue

            for letter in data[i]:
                if letter not in alp:
                    data.pop(i)
                    break

            else:
                data[i] = morph.parse(data[i])[0].normal_form
                i += 1

    def clear_str(txt: str):
        tokens = word_tokenize(txt.lower())
        delete(tokens)
        return " ".join(tokens)

    if type(file_text) is str:
        file_text = clear_str(file_text)

    elif '__iter__' in dir(file_text):
        file_text = list(file_text)

        for counter, text in enumerate(file_text):
            file_text[counter] = clear_str(text)

    return file_text
