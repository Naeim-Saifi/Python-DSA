class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class LL:
    def __init__(self) -> None:
        self.head=None

    def addF(self,data):
        
        newNode=Node(data)

        if self.head==None:
            self.head=newNode
            return 
        else:
            newNode.next=self.head
            self.head=newNode
            return
        
        
    def display(self):
        if self.head==None:
            print("Linked List is Empty....")
        else:
            print("Linked List...")
            temp=self.head
            while temp!=None:
                print(f"{temp.data}",end="-->")
                temp=temp.next

    def rev(self):
        prev=None
        curr=self.head
        while(curr!=None):
           next=curr.next
           curr.next=prev
           prev=curr
           curr=next
        self.head=prev
        self.display()


    def revIdx(self,left,right):
        prev=None
        curr=self.head
        i=1
        while i!=left:
            prev=curr
            curr=curr.next
            i=i+1
        before=prev
        start=curr
        prev=None
        while i!=right+1:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            i=i+1
        if before:  # If left is not the head of the list
            before.next = prev
        else:  # If the sublist starts at the head of the list
            self.head = prev
        start.next = curr 
        self.display()





node=LL()
node.addF(5)
node.addF(4)
node.addF(3)
node.addF(2)
node.addF(1)
node.display()
print()
# print("After revrsing......")
# node.rev()

node.revIdx(1,4)