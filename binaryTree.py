from queue import Queue
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

    def build_binary_tree(self,data):
        # '#' 表示该节点没有
        # 默认输入数据没问题
        newnode=Node(data[0]);
        node_cur=Queue();

        self.root=newnode;
        node_cur.put(self.root);
        temp_node=Node(0);
        i=1;
        while(i<len(data)):
            cur=node_cur.get();
            if(data[i]!='#'):
                newnode=Node(data[i]);
                cur.lchild=newnode;
                node_cur.put(cur.lchild);
            else:
                if(cur==temp_node):
                    node_cur.put(temp_node);
                else:
                    cur.lchild = None;
                    node_cur.put(temp_node);

            if(not (i+1<len(data))):
                break;
            if(data[i+1]!='#'):
                newnode=Node(data[i+1]);
                cur.rchild = newnode;
                node_cur.put(cur.rchild);
            else:
                if (cur == temp_node):
                    node_cur.put(temp_node);
                else:
                    cur.rchild = None;
                    node_cur.put(temp_node);
            i=i+2;

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
            cursor=Queue();
            data=[]
            cursor.put(self.root);
            while(not cursor.empty()):
                cur=cursor.get();
                data.append(cur.data);
                if(cur.lchild!=None):
                    cursor.put((cur.lchild));
                if (cur.rchild != None):
                    cursor.put(cur.rchild);
                # 每一层从右往左遍历
                # if (cur.rchild != None):
                #     cursor.put(cur.rchild);
                # if (cur.lchild != None):
                #     cursor.put((cur.lchild));
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

    def height(self,root_node):
        if(root_node==None):
            return 0;
        height_left=self.height(root_node.lchild);
        height_right=self.height(root_node.rchild);
        return 1+(height_left if height_left>height_right else height_right);

    def __is_balance__(self,root_node):
        if(root_node==None):
            return True;
        height_left=self.height(root_node.lchild);
        height_right=self.height(root_node.rchild);
        if(abs(height_right-height_left)>1):
            return False;
        else:
            return self.__is_balance__(root_node.lchild) and self.__is_balance__(root_node.rchild);

    def is_balance(self):
        return self.__is_balance__(self.root);

if __name__ == '__main__':

    binaryTree1=BinaryTree();
    binaryTree1.build_binary_tree([1,2,3,4,5,6,'#']);#'#'表示无此节点  [1,2,3,'#',4,5,6,'#','#',7]
    binaryTree1.inorder_travelsal();
    binaryTree1.preorder_travelsal();
    binaryTree1.level_travelsal();
    print(binaryTree1.is_balance())