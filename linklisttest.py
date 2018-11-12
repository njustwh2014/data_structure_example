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



class LinkList():
    def __init__(self):
        self.head=0;
        self.length=0;
    def is_empty(self):
        if(self.head==0):
            return True;
        else:
            return False;

    def get_item(self,data):
        if(self.is_empty()==True):
            print("The LinkList is empty!");
            return -1;
        else:
            j=0;
            p=self.head;
            while(p.next!=0):
                if(data==p.data):
                    return j;
                else:
                    p=p.next;
                    j=j+1;
            if (data == p.data):
                return j;
            print("Objects that do not exist in the linked list!");
            return -1;

    def append(self,data):
        if(self.is_empty()==True):
            newNode=Node(data);
            self.head=newNode;
            self.length=self.length+1;
        else:
            newNode=Node(data);
            p=self.head;
            while(p.next!=0):
                p=p.next;
            p.next=newNode;
            self.length=self.length+1;

    def insert(self,data,index):
        if(index<0 and index>self.length):
            print("the index is wrong!");
            return False;
        j=0;
        p=self.head;
        while(j<index):
            p=p.next;
            j=j+1;
        newNode=Node(data);
        pnext=p.next;
        p.next=newNode;
        newNode.next=pnext;
        self.length=self.length+1;
        return True;

    def get_length(self):
        return self.length;

    def delete(self,data):
        if(self.get_item(data)==-1):
            print("Objects that do not exist in the linked list!");
            return False;
        p=self.head;
        pfront=0;
        if(self.head.data==data):
            self.head=0;
            self.length=0;
            return True;
        pfront=p;
        p=p.next;
        while(p.next!=0):
            if(p.data==data):
                pfront.next=p.next;
                self.length=self.length-1;
                return True;
            else:
                pfront=p;
                p=p.next;
        if(p.data==data):
            pfront.next = p.next;
            self.length = self.length - 1;
            return True;
        return False;
    def printAll(self):
        if(self.length==0):
            print("the linklist is empty!");
            return ;
        p=self.head;
        print("there are {} nodes:".format(self.length));
        while(p.next!=0):
            print(p.data,end=" ");
            p=p.next;
        print(p.data);
        return ;

    def reorderList(self):
        if self.head == 0 or self.head.next == 0:
            return
        pre = self.head
        lat = self.head.next
        while lat != 0 and lat.next != 0:
            pre = pre.next
            lat = lat.next.next
        # self.printAll();
        p = pre.next
        pre.next = 0
        # reverse

        cur = 0
        while p != 0:
            q = p.next
            p.next = cur
            cur = p
            p = q
        # self.printAll();
        pre = self.head
        while pre != 0 and cur != 0:
            tmp = cur.next
            cur.next = pre.next
            pre.next = cur
            pre = pre.next.next
            cur = tmp
        # self.printAll();

    def reverseLinkList_self(self):
        curNode = self.head;
        prevNode = 0;
        nextNode = 0;
        reversedHead = 0;
        while (curNode != 0):
            nextNode = curNode.next;
            if (nextNode == 0):
                reversedHead = curNode;
            curNode.next = prevNode;
            prevNode = curNode;
            curNode = nextNode;
        self.head=reversedHead;

    def reverseLinkList(self,head):
        curNode=head;
        prevNode=0;
        nextNode=0;
        reversedHead=0;
        while(curNode!=0):
            nextNode=curNode.next;
            if(nextNode==0):
                reversedHead=curNode;
            curNode.next=prevNode;
            prevNode=curNode;
            curNode=nextNode;
        return reversedHead;

    def reorderLinkList(self):
        #1->2->3->4->5->None reorder 1->5->2->4->3->None
        #find mid Node
        #split LinkList to two parts
        #reverse later LinkList part
        #insert one by one
        if(self.length<2):
            return;
        slowNode=self.head;
        fastNode=self.head.next;
        while(fastNode!=0 and fastNode.next!=0):
            fastNode=fastNode.next.next;
            slowNode=slowNode.next;
        # find mid node
        midNode=slowNode.next;
        slowNode.next=0;
        midNode=self.reverseLinkList(midNode);
        slowNode=self.head;
        tempSlow=0;
        tempMid=0;
        while(slowNode!=0 and midNode!=0):
            tempSlow=slowNode.next;
            slowNode.next=midNode;
            tempMid=midNode.next;
            midNode.next=tempSlow;
            slowNode=tempSlow;
            midNode=tempMid;
    def SymmetryLinkList(self):
        if(self.length==0):
            return True;
        j=0;
        stack_prev=stack();
        p=self.head;
        jIndex=(int)(self.length/2);
        while(j<jIndex):
            stack_prev.push(p.data);
            j=j+1;
            p=p.next;
        if(self.length%2==0):
            if(p.data!=stack_prev.pop()):
                return False;
        p=p.next;
        while(p!=0):
            if(p.data!=stack_prev.pop()):
                return False;
            p=p.next;
        return True;
if __name__ == '__main__':
    # linklist1=LinkList();
    # # linklist1.printAll();
    # for i in range(10):
    #     linklist1.append(i);
    # for i in range(9,-1,-1):
    #     linklist1.append(i);
    # linklist1.printAll();
    # # linklist1.reorderList();
    # # linklist1.reorderLinkList();
    # linklist1.reverseLinkList_self();
    # linklist1.printAll();
    # print(linklist1.SymmetryLinkList());
    # linklist2=LinkList();
    # linklist2.append(1);
    # linklist2.append(2);
    # linklist2.append(3);
    # linklist2.append(4);
    # linklist2.append(3);
    # linklist2.append(2);
    # linklist2.append(1);
    # linklist2.printAll();
    # print(linklist2.SymmetryLinkList());
    stack1=stack();
    for i in range(10):
        stack1.push(random.randint(1,10))
    stack1.printAll();
    stack1.sort();
    stack1.printAll();


