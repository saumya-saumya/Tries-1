# Time : O(D * W) + O(S * L)

# insert operation :- D -> No. of words in Dictionary, W -> Length of Words in dictionary
# search and replace operation :- S -> No. of words in sentence, L -> Length of word in sentence
# Space : O(D * W) , size of Trie





class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        curr=self.root
        for ch in word:
            if curr.children[ord(ch)-ord('a')] is None:
                curr.children[ord(ch)-ord('a')]=TrieNode()
            curr=curr.children[ord(ch)-ord('a')]
        curr.isEnd=True
        
    def prefix(self,word):
        curr=self.root
        
        prefix=""
        for ch in word:
            if curr.children[ord(ch)-ord('a')] is None:
                return word
            else:
                curr=curr.children[ord(ch)-ord('a')]
                prefix+=ch
                if curr.isEnd:
                    return prefix
                
        return prefix
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
            
            
        result=sentence.split(" ")
        # print(result)
        for i in range(len(result)):
            pre=trie.prefix(result[i])
            # print(pre)
            if pre:
                result[i]=pre
        
        return " ".join(result)
