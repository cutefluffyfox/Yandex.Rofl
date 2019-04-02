from pandas import read_csv
from pymorphy2 import MorphAnalyzer
import string
from nltk import word_tokenize
from nltk.corpus import stopwords

city_csv = read_csv('../backend/csv/city.csv')
cities = list(city_csv['country_en'].apply(str))
cities.extend(list(city_csv['region_en'].apply(str)))
cities.extend(list(city_csv['city_en'].apply(str)))
cities.extend(list(city_csv['country'].apply(str)))
cities.extend(list(city_csv['region'].apply(str)))
cities.extend(list(city_csv['city'].apply(str)))
cities.extend(['ул'])
cities = list(set(map(str.lower, cities)))

names = list(read_csv('../backend/csv/surnames.csv')['Surname'].apply(str))
names.extend(list(read_csv('../backend/csv/rus_names.csv')['Name'].apply(str)))
names.extend(list(read_csv('../backend/csv/for_names.csv')['name'].apply(str)))
names = list(map(str.lower, names))


def tokenize_me(file_text, clean=True):
    def delete(data: list):
        deleted_words = []
        replace_words = ['***']

        morph = MorphAnalyzer()
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
        alp = 'йцукенгшщзхъэждлорпавыфячсмитьбюё1234567890' + string.ascii_letters

        i = 0

        while i < len(data):
            if data[i] in cities or data[i] in names or (clean and data[i] in stop_words) or\
                    (data[i][0] == '8' and len(data[i]) == 11):
                if data[i] == 'ул' and i + 1 < len(data):
                    deleted_words.append(data.pop(i + 1))
                    if not clean:
                        data.insert(i + 1, '***')

                deleted_words.append(data.pop(i))
                if not clean:
                    data.insert(i, '***')
                continue

            for letter in data[i]:
                if letter not in alp and data[i] not in replace_words:
                    deleted_words.append(data.pop(i))
                    if not clean:
                        data.insert(i, '***')
                    break

            else:
                if clean:
                    data[i] = morph.parse(data[i])[0].normal_form
                i += 1

        return deleted_words

    def clear_str(txt: str):
        tokens = word_tokenize(txt.lower())
        deleted_words = delete(tokens)
        return " ".join(tokens), deleted_words

    file_text, bad_words = clear_str(file_text)

    return file_text, bad_words


def to_normal_form(file_text):
    morph = MorphAnalyzer()
    out = []
    for word in word_tokenize(file_text.lower()):
        if word.isalnum():
            out.append(morph.parse(word)[0].normal_form)
    return " ".join(out)
