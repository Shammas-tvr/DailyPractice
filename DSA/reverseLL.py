class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def insert(self,val):
        if self.head is None:
            self.head=Node(val)
            return 
        curr=self.head
        while curr:
            if curr.next is None:
                curr.next=Node(val)
                return 
            curr=curr.next  


    def display(self):
        if self.head is None:
            return 

        curr=self.head 
        while curr:
            print(curr.val,end=" ")
            curr=curr.next
        return 

    def reverse(self):
        if self.head is None:
            return 
        curr=self.head
        prev=None

        while curr:
            nest=curr.next
            curr.next=prev
            prev=curr
            curr=nest
        self.head=prev
        return self.head

ll=LL()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)
ll.insert(70)
ll.insert(80)
ll.reverse()
ll.display()
