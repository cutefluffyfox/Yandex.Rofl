from pandas import read_csv
from nltk import word_tokenize

df = read_csv("clear_text1.csv")

a = read_csv('surnames.csv')
b = read_csv('rus_names.csv')
c = read_csv('for_names.csv')
a1 = list(a['Surname'].apply(str))
a1.extend(list(b['Name'].apply(str)))
a1.extend(list(c['name'].apply(str)))
a1 = list(map(str.lower, a1))


def tokenize_me(file_text):
    file_text = str(file_text )
    tokens = word_tokenize(file_text.lower())

    def delete_bad(data: list):
        i = 0
        while i < len(data):
            if data[i] in a1:
                data.pop(i)
            else:
                i += 1

    delete_bad(tokens)
    return " ".join(tokens)


check = df['clear_text'].apply(tokenize_me)

df['clear_text'] = check
df.to_csv("clear_text4.csv", encoding='utf-8')
