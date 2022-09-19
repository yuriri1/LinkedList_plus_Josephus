class Node:
    def __init__(self, val=None, _prox=None):
        self.value = val
        self.prox = _prox
        
class CircularLinkedList:
    def __init__(self):
        self.tail = None
        
    def is_empty(self):
        return self.tail is None
        
    def append(self, _val):
        novo = Node()
        novo.value = _val
        if self.is_empty():
            self.tail = novo
            novo.prox = self.tail
        else:
            p = self.tail.prox
            self.tail.prox = novo
            novo.prox = p
            
    def remove(self, val):
        if self.is_empty():
            return IndexError("Lista vazia")
        if self.tail.prox.value == val:
            p = self.tail.prox
            self.tail.prox = p.prox
        elif self.tail.value == val:
            p = self.tail.prox
            while p.prox is not self.tail:
                p = p.prox
            p.prox = self.tail.prox
            self.tail = p
        else:
            p = self.tail.prox
            while p is not self.tail:
                if p.prox.value == val:
                    p.prox = p.prox.prox
                    break
                p = p.prox
    
    
    def __str__(self):
        if self.is_empty():
            return "Lista vazia"
        else:
            p = self.tail.prox
            string = ""
            while p is not self.tail:
                string += str(p.value) + ", "
                p = p.prox
            string += str(p.value)
            return string
        
    def __len__(self):
        if self.is_empty():
            return 0
        else:
            p = self.tail.prox
            count = 1
            while p is not self.tail:
                p = p.prox
                count += 1
            return count
        
    def __iter__(self):
        if self.is_empty():
            return IndexError("Lista vazia")
        else:
            p = self.tail.prox
            while p is not self.tail:
                yield p.value
                p = p.prox
            yield p.value
                
import time

def josephus_problem(n,m):
    l = CircularLinkedList()
    
    for i in range(n,0, -1):
        l.append(i)

    for i in l:
        l.remove(i+1)

    print(l)

if __name__ == "__main__":
    start = time.time()
    josephus_problem(int(input()),int(input()))
    end = time.time()
    print(end - start)