class PrefixTree:

    def __init__(self):
        self.children = {} 
        self.is_end = False 

    def insert(self, word: str) -> None:
        # We insert
        node = self 
        for char in word: 
            if char not in node.children: 
                child = PrefixTree()
                node.children[char] = child 
            node = node.children[char] 
        node.is_end = True 

    def search(self, word: str) -> bool:
        node = self 
        for char in word: 
            if char not in node.children: 
                return False 
            else: 
                node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self 
        for char in prefix: 
            if char not in node.children: 
                    return False 
            else: 
                node = node.children[char]
        return True

        