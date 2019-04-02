from db import *
from sklearn.metrics.pairwise import cosine_similarity
from pymorphy2 import MorphAnalyzer
from time import time
from gensim.models.keyedvectors import Word2VecKeyedVectors
from numpy import frombuffer, float32
from random import shuffle

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
        """
        Начало таймера для проверки скорости работы определнного блока кода
        """
        global start
        start = time()

    def end_timer(text: str):
        """
        Конец таймера для проверки скорости работы определённого блока кода
        (Выводит в консоль)
        """
        global start
        this_time = time() - start
        print("-" * max(len(text), len(str(this_time)) + 4))
        print(this_time, "sec")
        print(text)
        print("-" * max(len(text), len(str(this_time)) + 4))

    print("#" * (len(str(phrase.split())) + 14))
    print(f"Entered data: {phrase.split()}")
    print("#" * (len(str(phrase.split())) + 14))

    start_timer()
    model = Word2VecKeyedVectors.load("../ml/russian_database")
    end_timer("Load rus database")

    db = DB()
    clean_table = CleanTable(db.get_connection())
    data = clean_table.get_all()

    minn = []
    try:
        main_vector = sum([model[f"{word}_{word_type(word)}"] if f"{word}_{word_type(word)}" in model.vocab
                           else 0 for word in phrase.split()]).reshape(1, -1)
    except AttributeError:
        main_text = set(phrase.split())
        out = []
        start_timer()
        for stroke in data:
            if len(set(stroke[2].split()) & main_text) >= len(main_text) // 3 + 1:
                out.append(stroke[1])
        shuffle(out)
        out = out[:10]
        end_timer(f"ERROR: Cannot transform all words to vector -> shuffle -> out: {out}")
        return out

    start_timer()
    for stroke in data:
        try:
            this_vector = [frombuffer(stroke[3], dtype=float32)]
            this = (cosine_similarity(this_vector, main_vector), stroke[1])
            if len(minn) < 5:
                minn.append(this)
            elif minn[0][0][0] < this[0][0]:
                minn[0] = this
                minn = sorted(minn, key=lambda a: a[0][0])
        except AttributeError:
            pass
        except ValueError:
            pass
    out = [out_data[-1] for out_data in minn[::-1]]
    end_timer(f"Word -> vec -> top5: {out}")
    return out

