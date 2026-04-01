class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    # Even though Python's OrderedDict does the same, we need to implement using Doubly Linked List
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = {}
        self.head = ListNode(-1,-1) #Sentinel Nodes (or Dummy Nodes)
        self.tail = ListNode(-1,-1) #Sentinel Nodes (or Dummy Nodes)
        # For empty list
        self.head.next = self.tail #Most Recently Used (MRU)
        self.tail.prev = self.head #Least Recently Used (LRU) 

    def add(self, node):
        # adding at the end of doubly linked list
        # real tail: tail.prev
        real_end = self.tail.prev
        real_end.next = node
        node.prev = real_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        # O(1) removal in doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.hash_table:
            return -1

        node = self.hash_table[key] #here the value in the hash table is the node
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            old_node = self.hash_table[key]
            self.remove(old_node)

        node = Node(key, value)
        self.hash_table[key] = node
        self.add(node)

        if len(self.hash_table) > self.capacity:
            # remove LRU, i.e., oldest, unused node which is the head (after the dummy head)
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.hash_table[node_to_delete.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)