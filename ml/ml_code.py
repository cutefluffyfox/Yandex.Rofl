"""
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО РАБОТАЕТ
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО РАБОТАЕТ КАК ВЫ ДУМАЕТЕ
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО НЕЛЬЗЯ ОПТИМИЗИРОВАТЬ
МЫ НЕ ГАРАНТИРУЕМ, ЧТО ЭТО СОВМЕСТИТСЯ С ВАШИМИ ПРОГРАММИСТАМИ И КОМПАНИЕЙ
"""


def ml():
    from pandas import read_csv
    from gensim.downloader import load as load_module
    from sklearn.metrics.pairwise import cosine_similarity
    import pymorphy2
    import time

    morph = pymorphy2.MorphAnalyzer()

    def word_type(word: str):
        return str(morph.parse(word)[0].tag).split(",")[0]

    def start_time():
        global start
        start = time.time()

    def end_time(name=""):
        global start
        print("------------------------")
        print(time.time() - start)
        print(name)
        print("------------------------")

    start_time()
    model = load_module('word2vec-ruscorpora-300')
    end_time("load")
    # model = gensim.models.Word2Vec.load("model.model.vectors.npy")
    # model.save("model.model")
    # print(0)
    # exit()

    start_time()
    df = read_csv(r"F:\трэш дата\final_text.csv")
    was = df["clear_text"][:4000]
    answers = df["Номер кейса"][:4000]

    numb = 4600
    test, answer = df["clear_text"][numb], df["Номер кейса"][numb]
    end_time("open and save")
    start_time()
    vec = (sum([model[f"{word}_{word_type(word)}"] if f"{word}_{word_type(word)}" in model.vocab else 0 for word in test.split()]), numb, test, answer)
    minn = [(cosine_similarity(sum([model[f"{word}_{word_type(word)}"] if f"{word}_{word_type(word)}" in model.vocab else 0 for word in was[0].split()]).reshape(1, -1), vec[0].reshape(1, -1)), 0, was[0], answers[0])]
    i = 1
    for phrase in was[1:]:
        try:
            this = (cosine_similarity(sum([model[f"{word}_{word_type(word)}"] if f"{word}_{word_type(word)}" in model.vocab else 0
                                           for word in phrase.split()]).reshape(1, -1), vec[0].reshape(1, -1)), i, phrase, answers[i])
            if len(minn) < 5:
                minn.append(this)
            elif minn[0][0][0] < this[0][0]:
                minn.append(this)
                minn = sorted(minn, key=lambda a: a[0][0])
                minn = minn[1:]
        except AttributeError:
            pass
        i += 1
    end_time("done")
    out = []
    for data in minn:
        out.append(data[-1])
    out.reverse()
    return out
    # Александр Сергеевич Кленин завалил стих про Ленина
    #
    # print(model.most_similar(minn[0], topn=1))


print(ml())
