class Trie:
    def __init__(self):
        self.children = {}
        self.end_of_folder = False

    def insert(self, path: str) -> None:
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True

    def prefix_search(self, path: str) -> bool:
        cur = self
        folders = path.split("/")
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.end_of_folder:
                return True
        return False


class Solution:
    # Date Solved: 4 August 2026, Tuesday
    # In NC All
    # Refer: NC and codestorywithMIK. NC uses Trie.
    # n = len(folder), m = length of each string
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        # Approach-1: NeetCode and similar to Approach 1 of codestorywithMIK
        # Time: O(n*m^2), Space: O(n*m) for set + result
        # For each folder of length m, scan up to m characters, and at each "/", build f[:i] (O(m) to slice) and hash it (O(m)). So each folder costs up to O(m^2), and across n folders that's O(n*m^2) time.
        res = []
        folder_set = set(folder)

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in folder_set:
                    res.pop()
                    break

        return res

        # Approach-2: Using Sorting (same for NC and codestorywithMIK)
        # Time: O(n*m*logn), Space: O(n) for result
        # Sorting n strings of avg length m costs O(n*logn) comparisons, each comparison up to O(m) -> O(n*m*logn). The single pass after sorting is only O(n*m) (one startswith check per folder, no nested loop).
        folder.sort()  # O(nlogn) comparisons, each O(m) -> O(n*mlogn)
        result = [folder[0]]  # sorted, so folder[0] can never be a sub-folder

        for i in range(1, len(folder)):
            currFolder = folder[i]
            lastFolder = result[-1] + "/"

            if not currFolder.startswith(lastFolder):
                result.append(currFolder)

        return result
        """
        # Approach-3: Trie
        # Time: O(n*m), Space:O(n*m)
        trie = Trie()
        for f in folder:
            trie.insert(f)

        res = []
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res
