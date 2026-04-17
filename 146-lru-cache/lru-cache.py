#I need a Node class to story the key and value and initalize my linkedlist
'''
U - I need to implement get and put in time of O(1) inorder to do this i will be using a hashmap for the key becuase look up is O(1) and 
    inorder to add / remove in O(1) I can use a linkedlist becuase it is O(1) evicition and addition if we know the position of the Node, 
    in order to have the positon everytime i remove i will map my hashmap as Key : Node pair 

M -> Hashmap + doublly LinkedList

P -> I will initailze a Node class to keep track of the key and value
    get will check if the key is in hashamp if not return 1
    if key in the dict now since we just used it 
    i will have to call my remove helper func on that Node which will remove the node 
    then i will call add to add it back at the tail.prev position whihc is my MRU 

'''
class Node:
    def __init__(self, key = 0 , val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        #now this are dummy nodes to handle edge cases and make it easier to add and remove
        self.head.next = self.tail
        self.tail.prev = self.head   

    def removeNode(self, Node):
        #give a node i will need to get the prev node make it point to the next node
        nodeToRemove = Node
        prevNode = nodeToRemove.prev
        nextNode = nodeToRemove.next
        #link the prev -> next and next to prev that way we can remove the node
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addNode(self, Node):
        #adding back is at the end right beofre tail
        nodeToAdd = Node
        prevNode = self.tail.prev
        nextNode = self.tail

        #now i want to add the node in between and link
        prevNode.next = nodeToAdd
        nodeToAdd.prev = prevNode
        #now link with the tail
        nodeToAdd.next = nextNode
        nextNode.prev = nodeToAdd


    def get(self, key: int) -> int:
        #check if the key not in the cache 
        if key not in self.cache:
            return -1
        else:
            #i have to call remove to unlink
            node = self.cache[key] 
            self.removeNode(node)
            #reattach back to the end to make it MRU
            self.addNode(node)
            #return the val of the node
            return node.val

    def put(self, key: int, value: int) -> None:
        #if the key, value not in cache then that is the first time so we just need to add in at the end
        if key not in self.cache:
            #we will just add to the linked list and cache
            node = Node(key, value)
            self.addNode(node)
            self.cache[key] = node
        else:
        #if the key exists then that is not the first time we need to ipdate the value and move to the end
            #we first remove 
            node = self.cache[key]
            self.removeNode(node)
            #update the val 
            nodeToAdd = Node(key, value)
            #reattach back 
            self.addNode(nodeToAdd)
            #update the cache
            self.cache[key] = nodeToAdd

        #check if the len of the cache is within capacity if not then we gotta evict
        if len(self.cache) > self.capacity:
            node = self.head.next
            #remove the LRU from linked list
            self.removeNode(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)