from pandas import read_csv
from nltk import word_tokenize
import string
df = read_csv("final_text.csv")


def tokenize_me(file_text):
    file_text = str(file_text)
    tokens = word_tokenize(file_text.lower())
    a1 = list('йцукенгшщзхъэждлорпавыфячсмитьбюё1234567890' + string.ascii_letters)
    a1.extend(['понедельник', 'вторник', 'среда°', 'четверг', 'пятница', 'суббота', 'воскресенье', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'])

    def delete_bad(data: list):
        i = 0
        while i < len(data):
            delete = True
            if data[i] in a1:
                data.pop(i)
                continue
            for letter in data[i]:
                if letter not in '1234567890г':
                    delete = False
                    break
            if delete:
                data.pop(i)
            else:
                i += 1

    delete_bad(tokens)
    return " ".join(tokens)


check = df['clear_text'].apply(tokenize_me)

df['clear_text'] = check
df.to_csv("final_text.csv", encoding='utf-8')