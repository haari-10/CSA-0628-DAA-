class WordFilter:

    def __init__(self, words):

        self.words = words

    def f(self, pref, suff):

        answer = -1

        for i, word in enumerate(self.words):

            if word.startswith(pref) and \
               word.endswith(suff):

                answer = i

        return answer


wordFilter = WordFilter(["apple"])

print(wordFilter.f("a", "e"))