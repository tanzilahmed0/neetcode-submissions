class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_end = False 
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # If the char is not already in the trie, we create a new node 
        # and map the current character as a child of the current node 
        # Then we move the node to the child node 
        node = self.root
        for char in word: 
            if char not in node.children: 
                child = TrieNode()
                node.children[char] = child 
            node = node.children[char] 
        node.is_end = True 

    def search(self, word: str) -> bool:
        node = self.root
        for char in word: 
            if char not in node.children: 
                return False 
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix: 
            if char not in node.children: 
                return False 
            node = node.children[char]
        return True

        