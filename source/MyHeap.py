import random
class heap_min():
    def __init__(self,data=[]):
        self.data=data;
        self.size=len(data);
        self.__adjust__(data);

    def is_empty(self):
        if(self.size==0):
            return True;
        else:
            return False;
    def __adjust__(self,data):
        if(self.is_empty()):
            return ;
        self.data=data;
        size=self.size;
        child=1;
        parent=1;
        cur=(int)(size/2);
        while(cur>0):
            parent=cur;
            lchild=2*cur;
            rchild=2*cur+1;
            while(lchild<=size):
                minimum_index=lchild;
                if(rchild<=size and self.data[lchild-1]>self.data[rchild-1]):
                    minimum_index=rchild;
                if(self.data[parent-1]<=self.data[minimum_index-1]):
                    break;
                self.data[parent-1],self.data[minimum_index-1]=self.__swap__(self.data[parent-1],self.data[minimum_index-1]);
                parent=minimum_index;
                lchild=2*parent;
                rchild=2*parent+1;

            cur=cur-1;


    def __swap__(self,data1,data2):
        return data2,data1

    def insert(self,data):
        #上浮
        self.data.append(data);
        self.size=self.size+1;

        i=self.size;
        while(i!=1):
            parent=(int)(i/2);
            if(self.data[i-1]<self.data[parent-1]):
                self.data[parent - 1], self.data[i - 1]=self.__swap__(self.data[parent-1],self.data[i-1])
            i=(int)(i/2);

    def delete(self):
        if(self.is_empty()):
            return ;
        self.size = self.size - 1;
        if (self.size == 0):
            self.data.pop();
            return;
        self.data[0]=self.data.pop();
        i=1;
        while(i<=self.size):
            lchild = 2 * i;
            rchild = 2 * i + 1;

            ####
            minmum_index=lchild;
            if(lchild<=self.size):
                if(rchild<=self.size and self.data[lchild-1]>self.data[rchild-1]):
                    minmum_index=rchild;

                if(self.data[i-1]<=self.data[minmum_index-1]):
                    break;

                self.data[i-1],self.data[minmum_index-1]=self.__swap__(self.data[i-1],self.data[minmum_index-1]);
            else:
                break;
            i=minmum_index;

    def print(self):
        print(self.data);


class heap_max():
    def __init__(self,data=[]):
        self.data=data;
        self.size=len(data);
        self.__adjust__(data);

    def is_empty(self):
        if(self.size==0):
            return True;
        else:
            return False;
    def __adjust__(self,data):
        if(self.is_empty()):
            return ;
        self.data=data;
        size=self.size;
        child=1;
        parent=1;
        cur=(int)(size/2);
        while(cur>0):
            parent=cur;
            lchild=2*cur;
            rchild=2*cur+1;
            while(lchild<=size):
                maxmum_index=lchild;
                if(rchild<=size and self.data[lchild-1]<self.data[rchild-1]):
                    maxmum_index=rchild;
                if(self.data[parent-1]>=self.data[maxmum_index-1]):
                    break;
                self.data[parent-1],self.data[maxmum_index-1]=self.__swap__(self.data[parent-1],self.data[maxmum_index-1]);
                parent=maxmum_index;
                lchild=2*parent;
                rchild=2*parent+1;

            cur=cur-1;


    def __swap__(self,data1,data2):
        return data2,data1

    def insert(self,data):
        #上浮
        self.data.append(data);
        self.size=self.size+1;

        i=self.size;
        while(i!=1):
            parent=(int)(i/2);
            if(self.data[i-1]>self.data[parent-1]):
                self.data[parent - 1], self.data[i - 1]=self.__swap__(self.data[parent-1],self.data[i-1])
            i=(int)(i/2);

    def delete(self):
        if(self.is_empty()):
            return ;
        self.size = self.size - 1;
        if(self.size==0):
            self.data.pop();
            return ;
        self.data[0]=self.data.pop();
        i=1;
        while(i<=self.size):
            lchild = 2 * i;
            rchild = 2 * i + 1;
            ####
            maxmum_index=lchild;
            if(lchild<=self.size):
                if(rchild<=self.size and self.data[lchild-1]<self.data[rchild-1]):
                    maxmum_index=rchild;

                if(self.data[i-1]>=self.data[maxmum_index-1]):
                    break;

                self.data[i-1],self.data[maxmum_index-1]=self.__swap__(self.data[i-1],self.data[maxmum_index-1]);
            else:
                break;
            i=maxmum_index;
    def print(self):
        print(self.data);



def get_median(data):
    if(len(data)==0):
        return [];
    heap_max_left=heap_max();
    heap_min_right=heap_min();
    ret=[];
    i=0;
    for i in range(len(data)):
        if(i==0):
            heap_max_left.insert(data[i]);
            ret.append(heap_max_left.data[0]);
        elif(i==1):
            if(data[i]<heap_max_left.data[0]):
                heap_min_right.insert(heap_max_left.data[0]);
                heap_max_left.delete();
                heap_max_left.insert(data[i]);
            else:
                heap_min_right.insert(data[i]);
            ret.append((heap_min_right.data[0]+heap_max_left.data[0])/2);
        else:
            if(heap_max_left.size==heap_min_right.size):
                if(data[i]>heap_min_right.data[0]):
                    temp=heap_min_right.data[0];
                    heap_min_right.delete();
                    heap_min_right.insert(data[i]);
                    heap_max_left.insert(temp);
                    ret.append(heap_max_left.data[0]);
                else:
                    heap_max_left.insert(data[i]);
                    ret.append(heap_max_left.data[0]);
            else:
                if(data[i]<heap_max_left.data[0]):
                    temp=heap_max_left.data[0];
                    heap_max_left.delete();
                    heap_max_left.insert(data[i]);
                    heap_min_right.insert(temp);
                    ret.append((heap_min_right.data[0] + heap_max_left.data[0]) / 2);
                else:
                    heap_min_right.insert(data[i]);
                    ret.append((heap_min_right.data[0] + heap_max_left.data[0]) / 2);
        print("index:{},max_heap:{},min_heap:{}".format(i,heap_max_left.data,heap_min_right.data))
    return ret;


def findmin10(data):#作业四:7.在N（N>=10万）个随机产生的数（对数的类型和范围没有限制）中找10个最小数，要求比较次数不大于1.2N。
    heap_max_1=heap_max(data[0:9]);
    for i in range(10,len(data)):
        if(data[i]<heap_max_1.data[0]):
            heap_max_1.delete();
            heap_max_1.insert(data[i]);
    return heap_max_1.data;
if __name__ == '__main__':

    # heap_min1=heap_min([79,66,43,83,30,87,38,55,91,72,49,9])
    # heap_min1.print();
    # heap_min1.insert(1);
    # heap_min1.print();
    # heap_min1.delete();
    # heap_min1.print();
    # print("*********************************************")
    # heap_max1=heap_max([6,4,5,3])
    # heap_max1.print();
    # heap_max1.insert(100);
    # heap_max1.print();
    # heap_max1.delete();
    # heap_max1.print();
    # heap_max1.delete();
    # heap_max1.print();
    #
    # print("*********************************************")
    #
    # data=[6, 4, 5, 8, 7, 9, 3, 4, 1, 2, 5, 8]
    # ret=get_median(data);
    # print(ret);
    data=[];
    for i in range(100000):
        data.append(random.randint(1,100000));
    ret=findmin10(data);
    print(ret);