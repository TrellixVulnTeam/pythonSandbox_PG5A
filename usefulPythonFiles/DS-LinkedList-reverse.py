class Node:
  def __init__(self, data):
    self.data = data
    self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return


    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None

# def reverse(lst):
#     if lst.is_empty():
#         return lst
    
#     cur = lst.get_head()

#     while cur.next_element: 
#         prev = cur
#         nex = cur.next_element.next_element
#         temp = cur.next_element
#         cur.next_element = prev
#         cur = temp

#     return lst #?

def reverse(lst):
  # To reverse linked, we need to keep track of three things
  previous = None # Maintain track of the previous node
  current = lst.get_head() # The current node
  next = None # The next node in the list

  #Reversal
  while current:
    next = current.next_element
    current.next_element = previous
    previous = current
    current = next

    #Set the last element as the new head node
    lst.head_node = previous
  return lst

#LC
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:       
#     prev = None
#     cur = head
#     next = None
    
#     while cur: 
#         next = cur.next
#         cur.next = prev
#         prev = cur
#         cur = next
        
#     return prev