class LL:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class Node:
    def __init__(self):
        self.head=None
    
    def addF(self,data):
        newNode=LL(data)
        if(self.head==None):
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
    def palin(self):
        li=""
        temp=self.head
        while temp!=None:
            li+=str(temp.data)
            temp=temp.next
        
        if li==li[::-1]:
            print("palindrome")
        else:
            print("Not")
    

    def nodeLen(self):
        length=0
        currNode=self.head
        while(currNode!=None):
            length+=1
            currNode=currNode.next
        print(f"Length of list : {length}")
        mid=(length//2)+1
        i=1
        currNode=self.head
        while(i<mid):
            currNode=currNode.next
            i+=1
        while(currNode!=None):
            print(f"{currNode.data}",end='-->')
            currNode=currNode.next
    
    def dele(self,data):
        currNode=self.head
        while currNode!=None:
            if currNode.data==data:
                


node=Node()
node.addF(1)
node.addF(2)
node.addF(3)
node.addF(2)
node.addF(1)
node.display()
node.palin()
print()
node.nodeLen()