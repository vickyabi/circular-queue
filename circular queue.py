from unittest.test.testmock.testwith import something_else


class Queue:
    def __init__(self,limit):
        self.queue=[]
        self.rear=0
        self.front=0
        self.limit=limit
    def isempty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def enqueue(self,item):
        if len(self.queue)==self.limit:
            print("the queue is full")


        else:
            if self.front==self.limit:
                self.front=self.rear-1

            self.queue.insert(self.front,item)
            self.front+=1
    def dequeue(self):
        if len(self.queue)==0:
            print("the stack is under flow")
        else:
            if self.rear==self.limit:
                self.rear=0
            self.queue.pop(self.rear)
            self.rear+=1
    def display(self):
        print(self.queue)
a=Queue(int(input("enter the limit of circular queue:")))
while True:

    print("1.enqueue \n2.dequeue \n3.display")
    ch=int(input("enter the choice:"))
    if ch==1:
        item=input("enter the element to enqueue:")
        a.enqueue(item)
    elif ch==2:
        a.dequeue()
    elif ch==3:
        a.display()
    else:
        print("invalid input!!! \n"
              "please enter the valid input")



