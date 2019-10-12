class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class linkedlist(object):
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = node(data)
        if self.head == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
  
    def insert(self,data):
        new_node = node(data)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)


    def printll(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


new = linkedlist()
new.insert_at_begin('10')
new.insert_at_begin('10')
new.insert_at_begin('10')
new.insert('20')
new.printll()


