#create a class to represent a node (just like struct Node from CS50 C programming)
#data that the current node is storing
#next node to point to the next node on the list

class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data nad the link to the next node in the list
    """
    data = None 
    next_node = None

    def __init__(self, data):
        self.data = data
    """
    A function that gets the inputed data and stores it as the data inside the Node
    """
    def __repr__(self):
        return "<Node data: %s>" % self.data
    """
    A function that prints out the <Node data: (%s meaning a placeholder for the string to be printed)> (% self.data == is the data that will be inside the string)
    """

class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None # when creating a linked list, assign the head value as None

    def isEmpty (self):
        return self.head == None 

    def size(self):
        """
        returns the number of nodes in the list
        takes 0(n) time or Linear time
        """
        current = self.head # make a variable that will loop and assign it the value of the head
        count = 0   # a variable that will increment each time a node is passed

        while current != None: # while the value is not None (not on the tail)
            count += 1 
            current = current.next_node # go to the next node after incrementing
        return count # return how many increments were made to see the size of the linked list
    def add(self, data):
        """
        adds a new node cointaining data at the head of the list
        takes 0(1) time or Constant time
        """
        new_node = Node(data) # create a proxy node that contains the data
        new_node.next_node = self.head # create a pointer to the current head of the list to connect the two
        self.head = new_node # replace the current head node with the new node 
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        return the node or None if not found
        Takes 0(n) time or Linear time
        """
        current = self.head # get the head node 

        while current != None:  # if the head not is not empty, execute the search function
            if current.data == key: # if current node is equal to the key being searched
                return current # return the value/data of the current node
            else:
                current = current.next_node # if not, go to the next node
        return None # return None if the key is not found on the linked list
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        insertion takes 0(1) Constant time but finding the node at the insertion point takes 0(n) Linear time
        Therefore it takes an overall Linear time
        """
        if index == 0: # if the index being inserted at is 0, it means it has to be inserted at the head
            self.add(data)
        if index > 0: # if the index greater than 0
            new = Node(data) # get the data being inserted and hold it on a temporary node
            position = index # get the index being inserted into and hold it 
            current = self.head # get the head of the list
            while position > 1: # traverse the list till the position(index) matches the order of the node in the list by decrementing on a loop
                current = current.next_node
                position -= 1
            prev_node = current # get the link of the current node and hold it
            next_node = current.next_node # get the link of the next_node of the current node and hold it
            prev_node.next_node = new # insert the data to the next_node of the placeholder link (current position of the current node)
            new.next_node = next_node   # insert the link of the placeholder next_node link to the next_node of the new data node 
    def remove(self,key):
        """
        Removes node containing data that matches the key 
        return the node or none if the key doesnt exist
        this takes 0(n) Linear time
        """
        current = self.head # get the head node of the list
        previous = None # set previous value as None
        found = False   # set found as False

        while current != None and not found:    # if the list is not empty AND if found = True
            if current.data == key and current is self.head:    # if the key and the current data matches and if it is the head of the list
                found = True    # set found to True
                self.head = current.next_node      # set the link of the head of the list to the current.next_node. This will unlink the previous head data to the list and remove it
            elif current.data == key:   # if data is not the head node
                found = True
                previous.next_node = current.next_node  # link the previous.next_node to the currents.next_node. This will unlink the current node to the list and remove it
            else:   # if the key and node does not match/ keep traversing
                previous = current  
                current = current.next_node
        return current
    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = [] # create a proxy list
        current = self.head # create a proxy variable and assign it the current head node
        while current != None: # while the node value is not None (not the tail)
            if current is self.head: # if the current value of the proxy node is equal to the value of the true head node
                nodes.append("[Head: %s]" % current.data) # create a string plus the data of the current value of the head node
            elif current.next_node is None: # if the node is at the tail
                nodes.append("[Tail: %s]" % current.data) # create a string plus the data of the current value of the tail node
            else:   # if the node is in between the head and tail node
                nodes.append("[%s]" % current.data) # create a string plus the data of the current node
            current = current.next_node # go to the next node at the end of everyloop to continue
        return  '-> '.join(nodes) # join all the strings appended with '->' and return the proxy list(nodes) to print out the strings and matching values

"""
N1 = Node (10)
print(N1)
N2 = Node (20) # create a new node with a new data
N1.next_node = N2 # point the link of the n1 node to the new n2 node 
print(N1.next_node) # print out and see the value inside the link of the next_node of the first n1 node if it is the n2 node data 
"""

"""
l = LinkedList()
N1 = Node (10)
l.head = N1
print(l.size())
N2 = Node (20)
N1.next_node = N2
print (l.size())
"""

"""
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l.size())
"""

"""
# this is called Prepending, it takes 0(1) Constant time
l = LinkedList()
l.add(10) # the first data added becomes the tail
l.add(20)
l.add(30)
l.add(40)
print(l)
"""

"""
l = LinkedList()
l.add(10)
l.add(20)
l.add(30)
l.add(40)
n = l.search(20)
print(n)
m = l.search(25)
print(m)
"""

"""
l = LinkedList()
l.add(10)
print(l)
l.insert(20,0)
print(l)
l.insert(30,0)
print(l)
l.add(40)
print(l)
l.insert(5,3)
print(l)
l.insert(18,1)
print(l)
l.add(50)
print(l)
l.remove(18)
print(l)
l.remove(5)
print(l)
n = l.remove(25)
print(n)
m = l.remove(50)
print(m)
print(l)
"""