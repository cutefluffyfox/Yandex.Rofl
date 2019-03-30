from backend.function_for_clean import tokenize_me
from gensim.models.keyedvectors import Word2VecKeyedVectors
from database.db import *
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
model = Word2VecKeyedVectors.load("russian_database")


def word_type(word: str) -> str:
    """
    Получает на вход слово, возращает его часть речи.
    """
    return str(morph.parse(word)[0].tag).split(",")[0]


def phrase_to_vector_to_str(phrase: str):
    try:
        return sum(model[f"{word}_{word_type(word)}"]
                   if f"{word}_{word_type(word)}" in model.vocab
                   else 0 for word in phrase.split()).reshape(1, -1).tostring()
    except AttributeError:
        return


database = DB()
cleaning_table = DataToCleaning(database.get_connection())
clean_table = CleanTable(database.get_connection())

while True:
    data = cleaning_table.get()

    if data:
        text = tokenize_me(data[2])

        if text[0]:
            clean_table.insert(data[1], text[0])
            clean_table.add_vector(data[1], phrase_to_vector_to_str(text[0]))


