# Date Solved: 13 August 2026, Thursday
# Refer: codestorywithMIK
# Approach: Using Trie
# Time: O(N * L * ClogC), N = total paths, L = average length of each path, C is the average number of children per node
# Space: ~O(N * L), we store all the paths in the trie, approximated value.
class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.subFolder = ""
            self.children = {}

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = self.Node("/")

        # Construct trie
        for path in paths:
            self.insert(root, path)

        subFolderMap = {}
        self.populateNodes(root, subFolderMap)

        self.removeDuplicates(root, subFolderMap)

        result = []
        self.constructResult(root, [], result)

        return result

    def insert(self, root, path):
        for folder in path:
            if folder not in root.children:
                root.children[folder] = self.Node(folder)
            root = root.children[folder]

    def populateNodes(self, root, subFolderMap):
        subFolderPaths = []

        for childName, child in root.children.items():
            subFolderResult = self.populateNodes(child, subFolderMap)
            subFolderPaths.append((childName, subFolderResult))

        subFolderPaths.sort()

        completePath = ""
        for childName, childPath in subFolderPaths:
            completePath += "(" + childName + childPath + ")"

        root.subFolder = completePath

        if completePath:
            if completePath in subFolderMap:
                subFolderMap[completePath] += 1
            else:
                subFolderMap[completePath] = 1

        return completePath

    def removeDuplicates(self, root, subFolderMap):
        childNames = []
        for childName in root.children:
            childNames.append(childName)

        for childName in childNames:
            child = root.children[childName]

            if child.subFolder != "" and subFolderMap[child.subFolder] > 1:
                del root.children[childName]
            else:
                self.removeDuplicates(child, subFolderMap)

    def constructResult(self, root, path, result):
        for childName, child in root.children.items():
            path.append(childName)
            result.append(list(path))
            self.constructResult(child, path, result)
            path.pop()
