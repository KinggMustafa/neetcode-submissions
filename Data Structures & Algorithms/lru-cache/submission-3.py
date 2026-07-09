class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.dummyhead = Node(0,0)
        self.dummytail = Node(0,0)
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead

    def get(self, key: int) -> int:
        value = self.store.get(key, None) #o(1) lookup
        #this node becomes top priority
        if value == None:
            return -1
        node = self.store[key]
        #remove
        previous = node.prev
        nxt = node.next
        previous.next = nxt
        nxt.prev = previous
        #insert our node to the head
        oldhead = self.dummyhead.next
        self.dummyhead.next = node
        node.next = oldhead
        node.prev = self.dummyhead
        oldhead.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].val = value
            node = self.store[key]
            previous = node.prev
            nxt = node.next
            previous.next = nxt
            nxt.prev = previous
        else:
            self.store[key] = Node(key, value) #create a new node for our new key
        node = self.store[key]
        oldhead = self.dummyhead.next
        self.dummyhead.next = node
        node.prev = self.dummyhead
        node.next = oldhead
        oldhead.prev = node

        if len(self.store) > self.capacity:
            tail = self.dummytail.prev
            newtail = tail.prev
            newtail.next = self.dummytail
            self.dummytail.prev = newtail
            del self.store[tail.key]
        

#we used a doubly linked list for o(1) lookup
#o(n) space where n is the length of puts
        
        
