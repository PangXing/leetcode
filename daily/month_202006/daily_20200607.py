# coding:utf-8

import copy
import collections

'''
【126. 单词接龙 II】
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:
    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
'''
class Solotion(object):
    def init(self, begin_word, endWord, word_list):
        self._res_list = list()
        self._cur_llist = [[begin_word]]
        self._end_word = endWord
        self._word_list = word_list
        self._graph = self.build_graph(begin_word, word_list)

    def _is_edge(self, word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
            if cnt == 2:
                break
        if cnt == 1:
            return True
        else:
            return False

    def build_graph(self, begin_word, word_list):
        graph = dict()
        for i in word_list:
            tmp = list()
            for k in word_list:
                if self._is_edge(i, k):
                    tmp.append(k)
            graph[i] = tmp
        if begin_word not in graph:
            tmp = list()
            for k in word_list:
                if self._is_edge(begin_word, k):
                    tmp.append(k)
            graph[begin_word] = tmp
        return graph


    def _find_next_list(self, cur_list):
        res = list()
        word = cur_list[-1]
        for i in self._graph[word]:
            if i in cur_list:
                continue
            res.append(i)
        res_list = list()
        for i in res:
            tmp = copy.deepcopy(cur_list)
            tmp.append(i)
            res_list.append(tmp)
        return res_list

    def _find_ladders(self):
        flag = False
        for i in self._cur_llist:
            if i[-1] == self._end_word:
                self._res_list.append(i)
                flag = True
        if not flag:
            next_level_list = list()
            for i in self._cur_llist:
                next_level_list.extend(self._find_next_list(i))
            if next_level_list:
                self._cur_llist = next_level_list
                self._find_ladders()

    def _is_exit(self, word, wordList):
        for i in wordList:
            if i == word:
                return True
        return False

    def findLadders(self, beginWord, endWord, wordList):
        if not self._is_exit(endWord, wordList):
            return []
        self.init(beginWord, endWord, wordList)
        self._find_ladders()
        return self._res_list

    def findLadders1(self, beginWord, endWord, wordList):
        if not endWord in wordList:
            return []
        hash = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i] + "*" + word[i + 1:]].append(word)

        def edges(word):
            for i in range(len(word)):
                for newWord in hash[word[:i] + '*' + word[i + 1:]]:
                    if not newWord in marked:
                        yield newWord

        def findPath(end):
            res = []
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent] + curr)
            return res

        marked = set()
        path = collections.defaultdict(set)
        begin = set([beginWord])
        end = set([endWord])
        forward = True
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                forward = not forward
            temp = set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin = temp
            if begin & end:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = findPath(res)
                return res
        return []

if __name__ == '__main__':
    solution = Solotion()
    print solution.findLadders('hot', 'dog', ["hot","dog"])
    print solution.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"] )
    print solution.findLadders('hit', 'cog',  ["hot","dot","dog","lot","log"])
    print solution.findLadders('cet', 'ism',  ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem",
                                               "who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"])
    print solution.findLadders("qa", "sq",
     ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca",
     "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au",
     "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga",
     "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er",
     "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"])


