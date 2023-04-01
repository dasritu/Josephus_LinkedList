class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class circular:
    def __init__(self):
        self.head=None
    def insert_end(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.ref!=self.head:
                temp=temp.ref
            newnode.ref=temp.ref
            temp.ref=newnode
    def add_beg(self,x):
         newnode=node(x)
         temp=self.head
         if temp==None:
            newnode.ref=newnode
            self.head=newnode
         else:
            temp=self.head
            while temp.ref is not self.head:
                temp=temp.ref
            newnode.ref=temp.ref 
            temp.ref=newnode
            self.head=newnode
    def add_beforenth (self,value,pos):
        newnode=node(value)
        if pos==1:
            temp=self.head
            if temp==None:
               newnode.ref=newnode
               self.head=newnode
            else:
                 temp=self.head
                 while temp.ref is not self.head:
                    temp=temp.ref
                 newnode.ref=temp.ref 
                 temp.ref=newnode
                 self.head=newnode
        else:
            c=1
            temp=self.head
            while temp.ref!=self.head and c<pos-1:
                temp=temp.ref
                c=c+1
            newnode.ref=temp.ref
            temp.ref=newnode
    def after_nth(self,value,pos):
        newnode=node(value)
        temp=self.head
        c=1
        while temp.ref!=self.head and c<pos:
               temp=temp.ref
               c+=1
        newnode.ref=temp.ref
        temp.ref=newnode

    def del_beg(self):
        # temp=self.head
        # temp1=temp.ref
        # self.head=temp1
        temp=self.head
        second=self.head.ref
        if temp.ref==self.head:
            del(self.head)
            self.head=None
        else:
            while temp.ref!=self.head:
                temp=temp.ref
            temp.ref=second
            del(self.head)
            self.head=second
    def del_any_node(self,x):
        if self.head is None:
            print("List is Null")
        temp=self.head
        if self.head.data==x:
            temp1=temp.ref
            self.head=temp1   
        while temp.ref!=self.head:
            if temp.data==x:
                break
            prev=temp
            temp=temp.ref
        prev.ref=temp.ref

    def del_end(self):
        temp=self.head
        if temp.ref==self.head:
            del(self.head)
            self.head=None
        else:
            while(temp.ref.ref!=self.head):
                temp=temp.ref
            del(temp.ref)
            temp.ref=self.head
    
    def deln_node(self,pos):
        if pos==1:
           temp=self.head
           second=self.head.ref
           if temp.ref==self.head:
              del(self.head)
              self.head=None
           else:
                while temp.ref!=self.head:
                  temp=temp.ref
                temp.ref=second
                del(self.head)
                self.head=second  
        else:
            temp=self.head
            c=1
            while temp.ref!=self.head and c<pos:
                  prev=temp
                  temp=temp.ref
                  c+=1
            prev.ref=temp.ref
        return temp
            #del(temp)
    def kill_node(self,pos):
        c=1
        temp=self.head
        while temp.ref!=self.head:
            if c==pos:
                break
            temp=temp.ref
            c+=1
        return temp
    # def getKthNode(start, k):
    #    temp = start
    #    for i in range(1, k):
    #       temp = temp.ref
    #    return temp
    def isLastNode(self):
      if self.head.ref == self.head:
         return True
      else:
          return False
    def josephus_kill(self,pos):
        temp=self.head
        while temp.ref!=temp:
             c=1
             while c<pos:
                 prev=temp
                 temp=temp.ref
                 c+=1
             prev.ref=temp.ref
             temp=temp.ref
             #self.display()
        return temp.data
    def display(self):
        if self.head==None:
            print("The linked list is null ")
        else:
            currnode=self.head
            while currnode.ref!=self.head:
                print(currnode.data,end="->")
                currnode=currnode.ref
            print(currnode.data)



c=circular()
c.add_beg(1)
c.add_beg(2)
c.add_beg(3)
c.add_beg(8)
c.add_beg(9)
c.add_beg(10)
c.add_beg(5)
c.add_beg(2)
c.display()
index=c.josephus_kill(4)
print(index)