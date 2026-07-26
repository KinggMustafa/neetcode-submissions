class Node():
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
        

    def get(self, key: int) -> int:
        #if key does not exist return -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        #the tail of the cache has to be the most recently touched node so: 
        #first we wire out this node just in case its the current tail bc we can get a cycle
        node.prev.next, node.next.prev = node.next, node.prev
        oldtail = self.right.prev
        oldtail.next, self.right.prev = node, node
        node.prev, node.next = oldtail, self.right
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache: #if our key already exists
            node = self.cache[key]
            node.prev.next, node.next.prev = node.next, node.prev
            node.next, node.prev = None, None
            
            del self.cache[key]
        elif self.cap == len(self.cache):
            head = self.left.next
            head.prev.next, head.next.prev = head.next, head.prev
            head.next, head.prev = None, None
            del self.cache[head.key]
        
        self.cache[key] = Node(key, value)
        node = self.cache[key]
        oldtail = self.right.prev
        oldtail.next, self.right.prev = node, node
        node.prev, node.next = oldtail, self.right


        
        
        
        









        
