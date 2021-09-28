#Hash Table with collisions
#Chaining search Big O = O(n)
#Chaining stores a linked list at every location and appends elements into the linked list when it comes to a collision
class HashTable:
    def __init__(self):
        self.MAX = 10 #array of size 10
        self.arr = [[] for i in range (self.MAX)] #nitialize empty array
        
    #Get index   
    def get_hash(self, key): #key is a string
        h = 0 
        for char in key: #goes through each of the characters
            h += ord(char) #h is the sum of the ASCII values - ord function finds an ASCII value for the character
            return h % self.MAX #divide by the size of the list
        
    #Get an item from the hashmap
    def __getitem__(self, key):
        h = self.get_hash(key) #get the hash for that key
        #self.arr[h] returns the elements in the linked list
        for element in self.arr[h]: #run a for loop to find the appropriate value in that list
            if element[0] == key: #if the element matches then it returns element at index [1]
                return element[1]
    
    #Add an item into hashmap 
    def __setitem__(self, key, val):
        h = self.get_hash(key) #gives the hash for a given key
        #at index h we will have a linked list so we iterate through the linked list and find the right location to update the value
        #iterate through the linked list
        #Find if the key exists or not
        found = False
        for index, element in enumerate (self.arr[h]): #enumerate used to iterate through elements in array
            if len(element) == 2 and element[0] == key: #for this key you have an element so change the value in that element
                self.arr[h][index] = (key, val) #insert tuple at same location at that index store the key & val
                found = True #key is found/exist
                break #break out of loop
        if not found:
            self.arr[h].append((key, val)) #update the list 
            
    #Delete an element
    def __delitem__(self, key): #delete an element with a particular key
        h = self.get_hash(key) #get hash for that key
        for index, element in enumerate(self.arr[h]): #look for the index of that particular list - iterate through the list
            if element[0] == key: 
                del self.arr[h][index] #in list, delete at particular index


#Adding elements to the hashtable 
t = HashTable()
t['March 8'] = 150
t['March 6'] = 55
t['March 17'] = 90
t['March 10'] = 500

#Displaying a particular element in the hashtable
t['March 6']

#Deleting an element in the hashtable
del t['March 17']

#Displaying the elements in the hastable
t.arr

