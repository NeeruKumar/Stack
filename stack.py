class stack:
    class node:
        def __init__(self,data,next):
            self.data=data
            self.next=next
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,data):
        self.head=self.node(data,self.head)
        self.size+=1
    def pop(self):
        if self.size==0:
            return 'empty'

        x=self.head.data
        self.head=self.head.next
        self.size-=1
        return x
    def max(self):
        a=self.head.data
        temp=self.head
        while temp.next!=None:
            temp=temp.next
            if a<temp.data:
                a=temp.data
        print( a)
    def show(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next


s=stack()
s.push(10)
s.push(20)
s.push(12)
s.push(45)
s.push(23)
s.push(54)
s.show()
s.pop()
s.show()
print('#')
a=[]
a.append()
print(max(a))




