# coding:utf-8

class TrieNode(object):
    def __init__(self):
        self.flag = False
        self.child = {}

class Trie(object):
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word):
        cur = self._root
        for i in word:
            if i not in cur.child:
                cur.child[i] = TrieNode()
            cur = cur.child[i]
        cur.flag = True

    def isAWord(self, word):
        cur = self._root
        for i in word:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        return cur.flag

class Solution(object):
    def respace(self, dictionary, sentence):
        size = len(sentence)
        if not dictionary:
            return size
        trie = Trie()
        for w in dictionary:
            trie.insert(w)

        dp = [0]
        for i in range(1, size+1):
            dp.append(dp[i-1] + 1)
            for j in range(i):
                if trie.isAWord(sentence[j:i]):
                    dp[i] = min(dp[i], dp[j])
        return dp[size]


if __name__ == '__main__':
    solution = Solution()
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"
    print solution.respace(dictionary, sentence)







