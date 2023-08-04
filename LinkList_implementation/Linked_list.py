class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head= None
    def print_list(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
if __name__ == '__main__':
    ll= LinkedList()
    ll.head= Node(3)
    second= Node(2)
    third= Node(1)
    ll.head.next= second
    second.next= third
    print(ll.print_list())


        
        