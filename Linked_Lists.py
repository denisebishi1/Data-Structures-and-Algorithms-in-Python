#class represents a single element in the list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data #data which can contain any datatype
        self.next = next #pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None #head variable which points to the head of the linked list

 #printing the linked list
    def print(self):
        if self.head is None: #if the linked list is empty print the below statement
            print("Linked list is empty")
            return
        #if the list is not empty create a temporary variable itr (iterator) and assign self.head to it    
        itr = self.head
        linked_list_string = '' #create a string for the linked list
        while itr:
            linked_list_string += str(itr.data)+' --> ' if itr.next else str(itr.data) #in the string created above we will append the data in the string
            itr = itr.next #iterating throught the list one by one and in each iteration you want to print a value
        print(linked_list_string) #print that list

#Method: To get length of a linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

#Method: Inserting an element at the beginning - Big O = O(1)
    def insert_at_beginning(self, data): 
        node = Node(data, self.head) #node with value "data" | self.head is the current head of that node
        self.head = node

#Method: Inserting element at the end
    def insert_at_end(self, data):
        if self.head is None: #if head/linked list is empty
            self.head = Node(data, None) #node created using that data, data is none(or null) you're simply pointing to that node
            return
        #if the head or linked list is not empty then you want to iterate through the list and go to the end
        #create an itr to iterate through the list
        itr = self.head 

        while itr.next:
            itr = itr.next #so we keep iterating
        #if itr.next = null then we are at the end of the list
        itr.next = Node(data, None) #when at the last element then point it to the new node which is null

#Method:Insert value at an index 
    def insert_at(self, index, data):
        if index<0 or index>self.get_length(): #if element is less than zero and greater than the length of the linked list
            raise Exception("Invalid Index") #if those numbers then present the error that the index is invalid

        if index==0:  #trying to insert at beginning
            self.insert_at_beginning(data)
            return

        count = 0 #For other cases we have to keep a count
        itr = self.head
        while itr: #loop for iterator which goes through all the elements
            if count == index - 1: #when inserting a new element you want modify the next pointer of the previous element
                #at element prior to the element we want to insert at
                node = Node(data, itr.next) #previous element's next will be the new element's next
                itr.next = node
                break

            itr = itr.next
            count += 1 #update or increment count

#Method:Remove value at an index  
    def remove_at(self, index):
        if index<0 or index>=self.get_length(): #if element is less than zero and greater than the length of the linked list
            raise Exception("Invalid Index") #if those numbers then present the error that the index is invalid

        if index==0: #if trying to remove the head | remove the element at the begining of the linked list
            self.head = self.head.next #pointing to the next element
            return

        count = 0
        itr = self.head 
        while itr: #loop goes through each of the elements of the linked list
            #stop at the element prior to the element you're trying to remove and modify the links
            if count == index - 1:
                itr.next = itr.next.next
                break #break out of the loop

            itr = itr.next
            count+=1 #update the count

 #Method: Taking a list of values as input and creating a new linked list (wipe out values and insert)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list: #iterate to the linked list
            self.insert_at_end(data)

#main function // for displaying methods - might have to do one at a time :) 
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5) #Big O = O(1)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    ll.insert_values(["eggs", "bacon", "grits", "sausage"])
    #print( "length of list: ", ll.get_length()) #useful when trying to remove an element at a given index
    ll.remove_at(2) #remove at index 2
    ll.insert_at(0, "figs") #insert at an index
    ll.print() #print the linked list