# coding:utf-8

class TrieNode(object):
    def __init__(self):
        self.flag = False #是否是单词
        self.words = {}    #子树节点


class Trie(object):
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word):
        cur = self._root
        for i in word:
            if i not in cur.words:
                cur.words[i] = TrieNode()
            cur = cur.words[i]
        cur.flag = True

    def search(self, word):
        cur = self._root
        for i in word:
            if i not in cur.words:
                return False
            cur = cur.words[i]
        if cur.flag:
            return True
        return False

    def startsWith(self, prefix):
        cur = self._root
        for i in prefix:
            if i not in cur.words:
                return False
            cur = cur.words[i]
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print trie.search('apple')
    print trie.search('app')
    print trie.startsWith('app')
    trie.insert('app')
    print trie.search('app')
