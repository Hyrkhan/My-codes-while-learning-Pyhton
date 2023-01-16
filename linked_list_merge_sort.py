# this is how to import classes that is made from another file
from linkedList import LinkedList

def merge_sort(linked_list):
    """
    This function sorts a linked list in ascending order
    - first recursively divide the linked list into sublists containing a single node
    - repeatedly merge the sublists to produce sorted sublists until one remains
    returns a sorted linked list

    runs in 0(kn log n) 
    """

    if linked_list.size() == 1: # if the linked list size is 1, it means its already sorted
        return linked_list
    elif linked_list.head is None: # if the linked list has no data inside
        return linked_list
    
    lefthalf, righthalf = split(linked_list) # split the left and right of the linked list at midpoint
    left = merge_sort(lefthalf) # sort the left and right half and merge it, place it to a placeholder variable
    right = merge_sort(righthalf) 

    return merge(left, right) # call the merge function to merge the two sublists into one, sorting it in the process

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublist

    takes 0(k log n)
    """
    if linked_list is None or linked_list.head is None: 
        lefthalf = linked_list
        righthalf = None
        return lefthalf, righthalf
    else:
        size = linked_list.size() # get the size of the linked list
        mid = size // 2 # get the midpoint of the linked list by using floor divide "// 2"

        mid_node = linked_list.node_at_index(mid-1) # use the node_at_index function to find the midpoint-1 index of the linkedlist

        lefthalf = linked_list  # pass the linked list to the lefthalf variable
        righthalf = LinkedList()    # create a new linkedlist() and pass it to the righthalf variable
        righthalf.head = mid_node.next_node # pass the link of the midnode's next node(midpoint+1) of the linkedlist to righthalf
        mid_node.next_node = None   # terminate the link of midnode.nextnode
    
        return lefthalf, righthalf  # return the lefthalf and righthalf variables

def merge(left, right):
    """
    This function merges two linked list sorting by data in the nodes
    Returns a new merged list

    runs in 0(n) linear time
    """
    # create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    # add a fake head that is discarded later
    merged.add(0)
    # set current to the head of the linked list
    current = merged.head
    # obtain head nodes for left and right linked lists
    lefthead = left.head
    righthead = right.head
    # iterate over left and right until we reach the tail node of either
    while lefthead or righthead:
        # if the head node of left is None weve passed the tail
        # add the tailnode from right to merged linked list
        if lefthead is None:
            current.next_node = righthead
            # call next on right to set while loop condition to false
            righthead = righthead.next_node
        # if the head node of right is None weve passed the tail
        # add the tailnode from left to merged linked list
        elif righthead is None:
            current.next_node = lefthead
            # call next on left to set loop while condition to false
            lefthead = lefthead.next_node
        else:
            # not at either tail node
            # obtain node data to perfrom comparison operations
            leftdata = lefthead.data
            rightdata = righthead.data
            # if data on left is less than right, set current to left node
            if leftdata < rightdata:
                current.next_node = lefthead
                # move left head to next node
                lefthead = lefthead.next_node
            # if data on left is greater than right, set current to right node
            else:
                current.next_node = righthead
                # move right head to next node
                righthead = righthead.next_node
        # move current to next node
        current = current.next_node
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(130)
l.add(123)
l.add(66)
l.add(1)
l.add(42)
l.add(231)

print(l)

sortedlinkedlist = merge_sort(l)
print(sortedlinkedlist)