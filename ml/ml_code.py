from database.db import *
from sklearn.metrics.pairwise import cosine_similarity
from pymorphy2 import MorphAnalyzer
from time import time
from gensim.models.keyedvectors import Word2VecKeyedVectors

"""
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО РАБОТАЕТ
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО РАБОТАЕТ КАК ВЫ ДУМАЕТЕ
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО НЕЛЬЗЯ ОПТИМИЗИРОВАТЬ
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО СОВМЕСТИТСЯ С ВАШИМИ ПРОГРАММИСТАМИ И КОМПАНИЕЙ
"""


def ml(phrase: str) -> list:

    """
    Получает на вход строку с 'красивыми' данными разделённые пробелами, делает анализ запроса и возращает
    список топ-5 (от наиболее похожих до наименее похожих) номеров ошибок.
    """

    morph = MorphAnalyzer()

    def word_type(word: str) -> str:
        """
        Получает на вход слово, возращает его часть речи.
        """
        return str(morph.parse(word)[0].tag).split(",")[0]

    def start_timer():
        global start
        start = time()

    def end_timer(text: str):
        global start
        print("-----------------------------")
        print(time() - start)
        print(text)
        print("-----------------------------")

    start_timer()
    model = Word2VecKeyedVectors.load("russian_database")
    end_timer("Load rus database")

    db = DB()
    clean_table = CleanTable(db.get_connection())
    data = clean_table.get_all()

    answers = []
    was = []

    for _ in data:
        answers.append(_[1])
        was.append(_[2])

    start_timer()
    vec = sum([model[f"{word}_{word_type(word)}"] if f"{word}_{word_type(word)}" in model.vocab
               else 0 for word in phrase.split()]).reshape(1, -1)
    minn = []
    i = 0
    for phrase in was:
        try:
            this = (cosine_similarity(sum([model[f"{word}_{word_type(word)}"]
                                           if f"{word}_{word_type(word)}" in model.vocab
                                           else 0
                                           for word in phrase.split()]).reshape(1, -1),
                                      vec), i, phrase, answers[i])
            if len(minn) < 5:
                minn.append(this)
            elif minn[0][0][0] < this[0][0]:
                minn.append(this)
                minn = sorted(minn, key=lambda a: a[0][0])
                minn = minn[1:]
        except AttributeError:
            pass
        i += 1
    end_timer("Words -> vec -> top 5")
    start_timer()
    out = []
    for data in minn:
        out.append(data[-1])
    out.reverse()
    end_timer("Reverse")
    return out
#
#
# print(ml("кот собака"))
