class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.root
        for character in word:
            if character not in head.children:
                head.children[character] = TrieNode()
            head = head.children[character]
        head.end_of_word = True

    def search_head(self, word):
        head = self.root
        for character in word:
            if character not in head.children:
                return False, None
            head = head.children[character]
        return True, head
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        end_of_word, head = self.search_head(word)
        if end_of_word:
            if head.end_of_word:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        end_of_word, _ = self.search_head(prefix)
        return end_of_word
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)