class Node():
    def __init__(self,data):
        self.data=data;
        self.lchild=None;
        self.rchild=None;

class BinaryTree():
    def __init__(self):
        self.root=None;

    def is_empty(self):
        return True if self.root==None else False;

    def add(self,data):
        newnode=Node(data);
        if(self.is_empty()):
            self.root=newnode;
            return ;
        else:
            temp=[];
            temp.append(self.root);
            while True:
                cur = temp.pop();
                if(cur.lchild==None):
                    cur.lchild=newnode;
                    return ;
                elif(cur.rchild==None):
                    cur.rchild=newnode;
                    return ;
                else:
                    temp.append(cur.rchild);
                    temp.append(cur.lchild);
    def level_travelsal(self):
        # I think hierarchical traversal is similar to breadth-first search.
        if(self.is_empty()):
            print("the binary tree is empty!");
            return [];
        else:
            cursor=[]
            data=[]
            cursor.append(self.root);
            while(cursor!=[]):
                cur=cursor.pop();
                data.append(cur.data);
                if(cur.rchild!=None):
                    cursor.append(cur.rchild);
                if(cur.lchild!=None):
                    cursor.append((cur.lchild));
            print(data); #just for debug
            return data;

    def __preorder_travelsal__(self,root):
        if (root==None):
            return [];
        else:
            data=[root.data];
            data1=self.__preorder_travelsal__(root.lchild);
            data2=self.__preorder_travelsal__(root.rchild);
            return data+data1+data2;

    def __inorder_travelsal__(self,root):
        if (root == None):
            return [];
        else:
            data1 = self.__inorder_travelsal__(root.lchild);
            data = [root.data];
            data2 = self.__inorder_travelsal__(root.rchild);
        return data1+data+data2;

    def __postorder_travelsal__(self,root):
        if (root == None):
            return [];
        else:
            data1 = self.__postorder_travelsal__(root.lchild);
            data2 = self.__postorder_travelsal__(root.rchild);
            data = [root.data];
        return data1+data2+data;

    def preorder_travelsal(self):
        data=self.__preorder_travelsal__(self.root);
        print(data);
        return data;

    def inorder_travelsal(self):
        data=self.__inorder_travelsal__(self.root);
        print(data);
        return data;

    def postorder_travelsal(self):
        data=self.__postorder_travelsal__(self.root);
        print(data);
        return data;

if __name__ == '__main__':
    binaryTree1=BinaryTree();
    for i in range(10):
        binaryTree1.add(i);
    binaryTree1.level_travelsal();
    binaryTree1.preorder_travelsal();
    binaryTree1.inorder_travelsal();
    binaryTree1.postorder_travelsal();