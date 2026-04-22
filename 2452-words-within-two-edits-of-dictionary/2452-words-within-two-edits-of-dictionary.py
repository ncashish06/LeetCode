class Solution:
    # Date Solved: 21 April 2026, Tuesday
    # Brute force over Trie since constraints are small
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        matching_queries = []
        for query_word in queries:
            for dict_word in dictionary:
                edit_distance = 0

                for i in range(len(query_word)):
                    if query_word[i] != dict_word[i]:
                        edit_distance += 1
                    if edit_distance > 2:
                        break

                if edit_distance <= 2:
                    matching_queries.append(query_word)
                    break

        return matching_queries
