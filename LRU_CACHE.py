class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def __repr__(self) -> str:
        return f"{self.value}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def move_to_front(self, node):
        if node == self.head:
            return  # Node is already at the front
        
        if node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
    
    def remove_last(self):
        if not self.tail:
            return None
        
        removed = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return removed


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.usage_list = DoublyLinkedList()
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # Move node to front as it's recently used
            self.usage_list.move_to_front(node)
            return node.value
        return -1  # Or default value if needed
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.usage_list.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used item
                removed = self.usage_list.remove_last()
                del self.cache[removed.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.usage_list.add_to_front(new_node)


# Creating an LRU Cache with a capacity of 2
lru_cache = LRUCache(2)

# Putting key-value pairs into the cache
lru_cache.put(1, 1)
lru_cache.put(2, 2)

# Getting values from the cache using keys
value1 = lru_cache.get(1)  # This will return 1

# Adding more key-value pairs
lru_cache.put(3, 3)

value2 = lru_cache.get(2)  # This will return -1 (since key 2 was evicted)
lru_cache.put(4, 4)

value3 = lru_cache.get(1)  # This will return -1 (since key 1 was evicted)
value4 = lru_cache.get(3)  # This will return 3
value5 = lru_cache.get(4)  # This will return 4
