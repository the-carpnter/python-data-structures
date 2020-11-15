class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def touch(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def push(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert(self, arr):
        self.head = None
        for i in arr:
            self.push(i)
    
    def __len__(self):
        if self.head is None:
            return 'Linked List is Empty!'
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def pop(self, index=None):
        if self.head is None:
            return
        if index == None:
            itr = self.head
            while itr.next.next:
                itr = itr.next
            x = itr.next.data
            itr.next = None
            return x
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                x = itr.next.data
                itr.next = itr.next.next
                return x
            itr = itr.next
            count += 1
        
    def __str__(self):
        if self.head is None:
            return 'Linked List is Empty!'       
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next       
        return llstr + 'None'
    
    
    
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert(range(1,10))
    ll.push(10)
    ll.touch(0)
    ll.pop()
    ll.pop()
    print(ll)
    print(len(ll))


