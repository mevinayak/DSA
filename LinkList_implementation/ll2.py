class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        return temp
if __name__=='__main__':
    ll= llist()
    ll.head= Node(1)
    second= Node(2)
    third= Node(3)
    ll.head.next=second
    second.next=third
    print(ll.printlist())
            

        
        