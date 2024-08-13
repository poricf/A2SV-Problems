# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Trie_Node():
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

        
class WordDictionary:

    def __init__(self):
        self.root = Trie_Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Trie_Node()
            curr = curr.children[idx]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(idx, root):
            curr = root

            for i in range(idx ,len(word)):
                if word[i] == '.':
                    for j in range(26):
                        if curr.children[j]:
                            if dfs(i+1, curr.children[j]):
                                return True
                    return False

                else:
                    pos = ord(word[i]) - ord('a')
                    if not curr.children[pos]:
                        return False
                    curr = curr.children[pos]
            return curr.is_end

        return dfs(0, self.root)

                    
                    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)