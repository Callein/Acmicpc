import heapq


class Word:
    def __init__(self, word):
        self.word = word
        self.length = len(word)

    def __lt__(self, other):
        if self.length == other.length:
            return self.word < other.word
        return self.length < other.length

    def __repr__(self):
        return self.word

    def __eq__(self, other):
        return self.word == other.word

    def __hash__(self):
        return hash(self.word)


words = list(set(Word(input()) for i in range(int(input()))))
heapq.heapify(words)

while words:
    print(heapq.heappop(words))
