class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def __str__(self):
        if self.head is None:
            return 'Linked List is Empty'       
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next       
        return llstr + 'None'
    
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    print(ll)


