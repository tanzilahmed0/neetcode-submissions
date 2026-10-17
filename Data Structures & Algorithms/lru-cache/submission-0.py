class Node: 
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev 
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        # We initialize a hashmap to map the keys to the values 
        # And we can use a linked list to map which keys are most/least recently used 
        # We use dummy head and tail nodes so every single node has a prev and next pointer 
        # to simplify insertion and deletion 
        # Our hash map will store a tuple of the value and the reference to the actual node 
        self.cache = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.capacity = capacity


    def get(self, key: int) -> int:
        # When we use get, we update hashmap or return -1, but then we also need to update the 
        # pointers. so we reference the node that we stored in the he hashmap, then we need to 
        # remove the node from the linkedlist and put it as the tail 
        if key in self.cache: 
            node = self.cache[key][1]
            node.prev.next, node.next.prev = node.next, node.prev 
            node.prev, node.next, self.tail.prev.next = self.tail.prev, self.tail, node 
            self.tail.prev, self.tail.next = node, None 
            return self.cache[key][0] 
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        # We check if the key is in the map already, if it is, we just update the map 
        # If it's not, we have to check if adding it will exceed the capacity, if it does 
        # we can remove the head node. We add our most recently used key as the tail node 
        # {1: (10, 1), 2: (20, 2)
        # head->1->2-> tail
        #.    <- <- <-
        if key in self.cache: 
            curr = self.cache[key][1]
            self.cache[key] = (value, curr)
            curr.prev.next, curr.next.prev = curr.next, curr.prev 
        elif self.capacity != 0: 
            self.capacity -= 1 
        else:
            del self.cache[self.head.next.val]
            self.head.next.next.prev, self.head.next = self.head, self.head.next.next
            
            
        node = Node(key)
        self.cache[key] = (value, node)
        node = self.cache[key][1] 
        self.tail.prev.next = node
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev, self.tail.next = node, None 
        
        

        
