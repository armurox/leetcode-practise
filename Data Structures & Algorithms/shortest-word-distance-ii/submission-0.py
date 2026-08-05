class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # construct hash map of all indexes of words
        self.word_dict = defaultdict(list)
        for i in range(len(wordsDict)):
            self.word_dict[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        possible_vals = []
        possible_vals.append(abs(max(self.word_dict[word1]) - min(self.word_dict[word2])))
        possible_vals.append(abs(max(self.word_dict[word1]) - max(self.word_dict[word2])))
        possible_vals.append(abs(min(self.word_dict[word1]) - max(self.word_dict[word2])))
        possible_vals.append(abs(min(self.word_dict[word1]) - min(self.word_dict[word2])))
        return min(possible_vals)


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
