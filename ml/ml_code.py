from database.db import *
from gensim.downloader import load as load_module
from sklearn.metrics.pairwise import cosine_similarity
import pymorphy2

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

    morph = pymorphy2.MorphAnalyzer()

    def word_type(word: str) -> str:
        """
        Получает на вход слово, возращает его часть речи.
        """
        return str(morph.parse(word)[0].tag).split(",")[0]

    model = load_module('word2vec-ruscorpora-300')

    db = DB()
    clean_table = CleanTable(db.get_connection())
    data = clean_table.get_all()

    answers = []
    was = []

    for _ in data:
        answers.append(_[1])
        was.append(_[2])

    vec = sum([model[f"{word}_{word_type(word)}"] if f"{word}_{word_type(word)}" in model.vocab
               else 0 for word in phrase.split()])
    minn = [(cosine_similarity(sum([model[f"{word}_{word_type(word)}"]
                                    if f"{word}_{word_type(word)}" in model.vocab
                                    else 0 for word in was[0].split()]).reshape(1, -1),
                               vec.reshape(1, -1)), answers[0])]
    i = 1
    for phrase in was[1:]:
        try:
            this = (cosine_similarity(sum([model[f"{word}_{word_type(word)}"]
                                           if f"{word}_{word_type(word)}" in model.vocab
                                           else 0
                                           for word in phrase.split()]).reshape(1, -1),
                                      vec.reshape(1, -1)), i, phrase, answers[i])
            if len(minn) < 5:
                minn.append(this)
            elif minn[0][0][0] < this[0][0]:
                minn.append(this)
                minn = sorted(minn, key=lambda a: a[0][0])
                minn = minn[1:]
        except AttributeError:
            pass
        i += 1
    out = []
    for data in minn:
        out.append(data[-1])
    out.reverse()
    return out
