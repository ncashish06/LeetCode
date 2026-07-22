class Solution:
    # Date Solved: 22 July 2026, Wednesday
    # Refer: NeetCode solution for LC. 616 "Add Bold Tag in String"
    # Same as LC. 758 "Bold Words in String" which is this week's premium question.
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n  # bold[i] = True if s[i] should be bolded

        # Mark every index covered by any occurrence of any word
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)  # find next overlapping occurrence

        open_tag = "<b>"
        close_tag = "</b>"
        ans = []

        # Walk through s, inserting a tag only at the boundary of a bold run
        # (this is what keeps the tag count minimal / merges overlapping words)
        for i in range(n):
            # start of a bold run: current char is bold AND (first char, or previous char wasn't bold)
            if bold[i] and (i == 0 or not bold[i - 1]):
                ans.append(open_tag)

            ans.append(s[i])

            # end of a bold run: current char is bold AND (last char, or next char isn't bold)
            if bold[i] and (i == n - 1 or not bold[i + 1]):
                ans.append(close_tag)

        return "".join(ans)
