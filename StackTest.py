import random
class Node():
    def __init__(self,data=0,next=0):
        self.data=data;
        self.next=next;


class stack():
    def __init__(self):
        self.top=0;
    def is_empty(self):
        if(self.top==0):
            return True;
        else:
            return False;
    def TopItem(self):
        if(self.is_empty()):
            return ;
        else:
            return self.top.data;
    def push(self,x):
        newNode=Node(x,self.top);
        self.top=newNode;
    def pop(self):
        if(self.is_empty()):
            return ;
        else:
            ret=self.top.data;
            self.top=self.top.next;
            return ret;

    def printAll(self):
        # just used for debug
        if(self.is_empty()):
            print("the stack is empty!");
            return ;
        tempStack=stack();
        while(self.top!=0):
            print(self.top.data,end=" ");
            tempStack.push(self.pop());
        while(tempStack.top!=0):
            self.push(tempStack.pop());
        print("");
        return ;

    def sort(self):
        if (self.is_empty()):
            print("the stack is empty!");
            return;
        tempStack=stack();
        tempStack.push(self.pop());
        while(not self.is_empty()):
            x=self.pop();
            j=0;
            while(x<tempStack.TopItem()):
                j=j+1;
                self.push(tempStack.pop());
                if(tempStack.is_empty()):
                    break;
            tempStack.push(x);
            while(j!=0):
                tempStack.push(self.pop());
                j=j-1;
        while(not tempStack.is_empty()):
            self.push(tempStack.pop());

    def getStackBottomAndRemove(self):
        #use recursion
        #get stack bottom Item and remove it.
        x=self.TopItem();
        self.pop();
        if(self.is_empty()):
            return x;
        last=self.getStackBottomAndRemove();
        self.push(x);
        return last;
    def reverseStack(self):
        # reverse Stack by recursion
        if(self.is_empty()):
            return ;
        i=self.getStackBottomAndRemove();
        self.reverseStack();
        self.push(i);
        return ;

if __name__ == '__main__':
    stack1=stack();
    for i in range(10):
        stack1.push(random.randint(1,10))
    stack1.printAll();
    stack1.sort();
    stack1.printAll();
    stack1.reverseStack();
    stack1.printAll();