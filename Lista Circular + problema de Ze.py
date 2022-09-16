class Node:
    def __init__(self, val=None, _prox=None):
        self.value = val
        self.prox = _prox
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
        
    def append(self, _val):
        novo = Node()
        novo.value = _val
        if self.is_empty():
            self.head = novo
            novo.prox = self.head
        else:
            p = self.head
            while p.prox is not self.head:
                p = p.prox
            p.prox = novo
            novo.prox = self.head
            
    def remove(self, val):
        if self.is_empty():
            return IndexError("Lista vazia")
        if self.head.value == val:
            p = self.head
            while p.prox is not self.head:
                p = p.prox
            p.prox = self.head.prox
            self.head = self.head.prox
        else:
            p = self.head
            while p.prox is not self.head:
                if p.prox.value == val:
                    p.prox = p.prox.prox
                    break
                p = p.prox
    
    
    def __str__(self):
        if self.is_empty():
            return "Lista vazia"
        else:
            p = self.head
            string = ""
            while p.prox is not self.head:
                string += str(p.value) + " "
                p = p.prox
            string += str(p.value)
            return string
        
    def __len__(self):
        if self.is_empty():
            return 0
        else:
            p = self.head
            count = 1
            while p.prox is not self.head:
                p = p.prox
                count += 1
            return count
        
    def __iter__(self):
        if self.is_empty():
            return IndexError("Lista vazia")
        else:
            p = self.head
            while p.prox is not self.head:
                yield p.value
                p = p.prox
            yield p.value
                
import time

if __name__ == "__main__":
    start = time.time()
    l = CircularLinkedList()
    for i in range(100):
        l.append(i)

    for i in l:
        print(i)
        
    end = time.time()
    
    print(end - start)