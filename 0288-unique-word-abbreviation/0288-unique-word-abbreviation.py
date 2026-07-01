from collections import defaultdict


class ValidWordAbbr:
    # Date Solved: 1 July 2026, Wednesday, Weekly Premium W1
    def __init__(self, dictionary: List[str]):
        self.abbr_map = defaultdict(set)
        for word in dictionary:
            self.abbr_map[self._abbreviate(word)].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = self._abbreviate(word)
        words_with_abbr = self.abbr_map[abbr]

        # Case 1: no word in the dictionary has this abbreviation at all
        if len(words_with_abbr) == 0:
            return True

        # Case 2: for the condition to be true, there should be exactly one word in dictionary and that should match the given (query) word
        # if the word itself is the only one, and it's an exact match
        if len(words_with_abbr) == 1 and word in words_with_abbr:
            return True

        return False

    def _abbreviate(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
