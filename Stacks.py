#Last In First Out (LIFO)
#Push/Pop element is Big O(1)
#Searching element by value is O(n)

#create a list s
s = []
s.append('1')
s.append('2')
s.append('3')
s.append('4')

#Delete the last item
s.pop()

#Get last element
s[-1]

#Stack Implementation is better with collection.deque
#dir(stack) returns the types of methods 

from collections import deque #import deque
stack = deque

#Adds to the end of the list
stack.append('Why')

class Stack:
    def __init__(self):
        self.container = deque()
    
    #adds an element to a stack
    def push(self,val):
        self.container.append(val)
    
    #deletes an element in a stack   
    def pop(self):
        return self.container.pop()
    
    #returns the first element in a stack
    def peek(self):
        return  self.container[-1]
    
    #checks if stack is empty
    def is_empty(self):
        return len(self.container)==0
    
    #returns the size of the stack
    def size(self):
        return len(self.container)
    
s = Stack()
s.pop(5)