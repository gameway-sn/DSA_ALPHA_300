class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def sumPrefixScores(self, words):
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                node.count += 1

        ans = []

        for word in words:
            node = root
            score = 0

            for ch in word:
                node = node.children[ch]
                score += node.count

            ans.append(score)

        return ans
