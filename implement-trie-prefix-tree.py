# Time:
# insert(word): O(|word|)
# search(word): O(|word|)
# startsWith(prefix): O(|prefix|)
# Space: O(T), where T is total of Trie nodes, in the worst case it's total number of characters of words we inserted.
class Trie:

    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
        

    def insert(self, word: str) -> None:
        curr=self
        
        for ch in word:
            if curr.children[ord(ch)-ord('a')] is None:
                curr.children[ord(ch)-ord('a')] = Trie()
            curr=curr.children[ord(ch)-ord('a')]
        curr.isEnd=True

    def search(self, word: str) -> bool:
        curr=self
        
        for ch in word:
            if curr.children[ord(ch)-ord('a')] is None:
                return False
            curr=curr.children[ord(ch)-ord('a')]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr=self
        
        for ch in prefix:
            if curr.children[ord(ch)-ord('a')] is None:
                return False
            curr=curr.children[ord(ch)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
