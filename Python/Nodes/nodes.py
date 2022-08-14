class Node:
    #passed variables to constructor
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    #returns the value using self.value which otherwise wouldn't accessible to the method
    def get_value(self):
        return self.value
    #returns link_node using self. which otherwise wouldn't accessible to the method
    def get_link_node(self):
        return self.link_node
    #updates the link_node by passing it as an argument
    def set_link_node(self, link_node):
        self.link_node = link_node
#instantiates 3 nodes w/strings
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")
#uses each node to track the other
dot.set_link_node(wacko)
yacko.set_link_node(dot)
#variable stores the value of each node
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
#prints nodes values
print(dots_data)
print(wackos_data)

class Node:
    #gave constructor 2 variables
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
  def get_value(self):
    return self.value
  def get_next_node(self):
    return self.next_node
  def set_next_node(self, next_node):
    self.next_node = next_node
#creates an object from the class then passes the object a value
my_node = Node(44)
print(my_node.get_value())

class LinkedList:
    #constructor sets the head node
  def __init__(self, value=None):
    self.head_node = Node(value)
    #getter returns head node
  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    #instantiating the class into an object  
    new_node = Node(new_value)
    #linking the existing head to a new head
    new_node.set_next_node(self.head_node)
    #replacing the existing head with the new
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    #this variable calls the current head node
    current_node = self.get_head_node()
    #the while loop iterates through so long as the value of the current node isn't None
    while current_node:
      #adds the get_value to the current node
      if current_node.get_value() != None:
          #string_list is being added the values of the current_node
        string_list += str(current_node.get_value()) + "\n"
        #get_next_node is a built-in method that does this automatically, didn't know that.
      current_node = current_node.get_next_node()
    return string_list
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

#the method below is for removing a node, however, I could assemble it from scratch. It seems very complex.
def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node


class Node:
  def __init__(self, value, next_node=None, prev_node=None):
      #constructor sets the values for prev and next nodes as they will be assigned and accesssed
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    #these methods are what music player apps would need to move through songs as an example of utility
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
    #updates the head nodes
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    self.head_node = new_head
    if self.tail_node == None:
      self.tail_node = new_head
      
    #updates the tail nodes
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    
    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail
      
    #removes the head method
  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None
    #removes head node then checks for the next node
    self.head_node = removed_head.get_next_node()
    #verifies no nodes came before head node
    if self.head_node != None:
      self.head_node.set_prev_node(None)
    
    if removed_head == self.tail_node:
      self.remove_tail()
    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node
    #checks if removed_tail has no value
    if removed_tail == None:
      return None
    #sets tail node equal to removed_tail's previous node
    self.tail_node = removed_tail.get_prev_node()
    #if there is a node, then this statements sets the next node
    if self.tail_node != None:
      self.tail_node.set_next_node(None)
    #if removed_tail is equal to head_node then remove it
    if removed_tail == self.head_node:
      self.remove_head()
    return removed_tail.get_value()

def remove_by_value(self, value_to_remove):
    node_to_remove = None
    #setting current node to list's head
    current_node = self.head_node
    #the while loop ensures there is a cucrent_node
    while current_node != None:
      #the if statement removes the current node when it's value matches None
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
      #the 2 statements above are required conditions in order for the current to be updatable
      current_node = current_node.get_next_node()
    #returns the end of the method since there is no node to remove
    if node_to_remove == None:
      return None
    #checks if node being removed is at the head
    if node_to_remove == self.head_node:
      self.remove_head()
    #checks if the node being removed is at the tail
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      #with the 2 conditions above met, it means that the node to be removed is somewhere in the middle of the other nodes 
        next_node = node_to_remove.get_next_node()
        prev_node = node_to_remove.get_prev_node()
        next_node.set_prev_node(prev_node)
        prev_node.set_next_node(next_node)
    return node_to_remove

#Creates an object from DoublyLinkedList Class:
subway = DoublyLinkedList()
#Adds nodes to head of list
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
print(subway.stringify_list())
#Adds nodes to tail of list
subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
print(subway.stringify_list())
#Removes only the head & tail
subway.remove_head()
subway.remove_tail()
print(subway.stringify_list())
#Removes a node that is neither at the head or tail
subway.remove_by_value("Times Square")
print(subway.stringify_list())
