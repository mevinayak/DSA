class ListNode:
    def __init__(self, val):
        self.val= val
        self.next=None
        self.prev= None
class history:
    def __init__(self, homepage):
        self.home= ListNode(homepage)

    def visit(self, url):
        node= ListNode(url)        
        self.home.next = node
        node.prev= self.home
        self.home= self.home.next
    def back(self, steps):
        curr= self.home
        while curr.prev and steps>0:
            curr= curr.prev
            steps= steps-1
        self.home= curr
        return curr.val
    
    def forward(self, steps):
        curr= self.home
        while( curr.next and steps>0):
            curr= curr.next
            steps= steps-1
        self.home= curr
        return curr.val
    
