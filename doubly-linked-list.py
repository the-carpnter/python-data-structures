class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DlinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
        new_node.prev = itr
        

    def touch(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def pop(self, index = None):
        if index == 0:
            x = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return x

        if index is None or index == len(self)-1:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.prev.next = None
            itr.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                itr = None
                return
            itr = itr.next
            count += 1
    
    def delete(self, data):
        itr = self.head
        while itr:
            if itr.data == data and self.head.next is None:
                itr = None
                self.head = None
                return

            if itr.data == data and itr is self.head:
                self.head = itr.next
                itr.next.prev = None
                itr.next = None
                itr = None
                return
            
            if itr.data == data and itr.next is None:
                itr.prev.next = None
                itr.prev = itr.next = None
                itr = None
                return
            
            if itr.data == data:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                itr.next = itr.prev = None
                itr = None
                return
            
            itr = itr.next
    
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.touch(new_node.data)
            return
        
        if index == len(self):
            self.push(new_node.data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node.next = itr.next
                new_node.prev = itr
                itr.next.prev = new_node
                itr.next = new_node
                itr = None
                return
            itr = itr.next
            count += 1
             
    def __str__(self):
        if self.head is None:
            return 'List is Empty!'
        itr = self.head
        k = 'None -- ' 
        while itr:
            k += '[' + str(itr.data) + ']' + ' -- '
            itr = itr.next
        return k + 'None'

if __name__ == '__main__':
    dl = DlinkedList()
    for i in range(10):
        dl.push(i)
    print(dl)
    dl.insert(9, 100)
    print(dl)
    dl.pop(10)
    print(dl)