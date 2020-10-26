# class Node:
#     def __init__(self,data = None,next = None):
#         self.data  = data
#         self.next = next



# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insertAtBegining(self,data):
#         node = Node(data,self.head)
#         self.head = node

#     def traverse(self):
#         if self.head is None:
#             print("Linkedlist is empty")
#         else:
#             itr = self.head
#             llstr = ''
#             while itr:
#                 llstr += str(itr.data)+'---->'
#                 itr = itr.next
#         print(llstr+"null")
        

# if __name__ == "__main__":

#     ll = LinkedList() 
#     ll.insertAtBegining(45)
#     ll.insertAtBegining(12)
#     ll.insertAtBegining(8)
#     ll.insertAtBegining(5)
#     ll.traverse()       




class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head  = None
        self.tail  = None

    def insertAtBegining(self,data):
        if self.head is None:
            n0 = Node(data)
            self.head = n0
            self.tail = n0
        else:
            n0 = Node(data,self.head)
            n0.next = self.head
            self.head.prev = n0
            self.head = n0    
    def insertAtEnd(self,data):
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        n1 = Node(data,prev=temp)
        temp.next = n1
        n1.prev = temp
        self.tail = n1 
    def insertBetween(self,data):
        count = 0
        temp = self.head
        while temp.next!=None:
            count += 1
            temp = temp.next
        print("Available space ",count-1)

        # print(temp.data)    
        
        p = 0
        while p==0:
            indx = int(input("Enter the place to insert :"))
            if (indx == 1 or indx==0):
                print("Invalid choice you can't enter at the begining!!")
            elif indx == count+1:
                print("Invalid choice you can't enter at the end!!")
            else:
                p=1
        # print(indx)
        # print(temp.data)        
        # print(temp.data,count)
        while((indx-1)!=count):
            temp = temp.prev
            # print(temp.data)
            count-=1
        # print(count)
        temp1 = temp.next
        n2 = Node(data)
        temp.next = n2
        n2.prev = temp
        n2.next = temp1
        temp1.prev = n2


    def traverse(self):
        if self.head is None:
            print("No data present")
        else:
            itr = self.head
            val = ''
            while itr:
                val += str(itr.data)+'--->'
                itr = itr.next

        print("Null-->"+val+"Null")
                      

if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insertAtBegining(56)
    ll1.insertAtBegining(80)
    ll1.insertAtBegining(99)
    ll1.insertAtEnd(5)
    ll1.insertAtBegining(56)
    ll1.insertAtBegining(80)
    ll1.insertAtBegining(99)
    ll1.insertAtEnd(5)
    ll1.traverse()
    ll1.insertBetween(53)
    ll1.traverse()
    ll1.insertBetween(91)
    ll1.traverse()
    


    