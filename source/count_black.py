import numpy as np
from queue import Queue
import sys



def count_black(data):
    # 思路是遍历两边进行编号，按号码索引
    lenRow=data.shape[0]
    lenColumn=data.shape[1]
    index_found = np.zeros((lenRow,lenColumn),dtype=int)
    temp=int(0)
    for i in range(lenRow):
        for j in range(lenColumn):
            if(data[i][j]==True):
                if(i==0):#第一行特殊处理
                    if(j==0):
                        temp=temp+1
                        index_found[i][j]=temp #第一个数
                    else:
                        if(index_found[i][j-1]>0):
                            index_found[i][j]=index_found[i][j-1]
                        else:
                            temp=temp+1
                            index_found[i][j]=temp

                else:#其他行
                    if(j==0):
                        if(index_found[i-1][j]>0):
                            index_found[i][j]=index_found[i-1][j]
                        else:
                            temp=temp+1
                            index_found[i][j]=temp
                    else:
                        if(index_found[i-1][j]>0 and index_found[i][j-1]>0):
                            if(index_found[i-1][j]!=index_found[i][j-1]):
                                if(index_found[i-1][j]>index_found[i][j-1]):
                                    index_found[i-1][j]=index_found[i][j-1]
                                else:
                                    index_found[i][j-1]=index_found[i-1][j]
                                index_found[i][j]=index_found[i-1][j]
                            else:
                                index_found[i][j] = index_found[i - 1][j]
                        elif(index_found[i][j-1]>0 and index_found[i-1][j]==0):
                            index_found[i][j]=index_found[i][j-1]
                        elif (index_found[i][j - 1] == 0 and index_found[i - 1][j] > 0):
                            index_found[i][j] = index_found[i-1][j]
                        else:
                            temp = temp + 1
                            index_found[i][j] = temp

    #取局部最小值
    for i in range(lenRow):
        for j in range(lenColumn):
            xleft=sys.maxsize
            x=sys.maxsize
            xright=sys.maxsize
            xup=sys.maxsize
            xdown=sys.maxsize
            if(index_found[i][j]>0):
                x=index_found[i][j]
                if(i==0):#第一排
                    if(j==0):
                        #第一个数据
                        if(index_found[i][j+1]>0):
                            xright=index_found[i][j+1]
                        if(index_found[i+1][j]>0):
                            xdown=index_found[i+1][j]
                        x=min(xright,xdown,x)
                        index_found[i][j]=x
                        if (index_found[i][j + 1] > 0):
                            index_found[i][j + 1]=x
                        if (index_found[i + 1][j] > 0):
                            index_found[i + 1][j]=x
                    elif(j==lenColumn-1):
                        #第一排最后一列
                        if(index_found[i][j-1]>0):
                            xleft=index_found[i][j-1]
                        if(index_found[i+1][j]>0):
                            xdown=index_found[i+1][j]
                        x=min(x,xleft,xdown)
                        index_found[i][j]=x
                        if (index_found[i][j - 1] > 0):
                            index_found[i][j - 1]=x
                        if (index_found[i + 1][j] > 0):
                            index_found[i + 1][j]=x
                    else:
                        if(index_found[i][j-1]>0):
                            xleft=index_found[i][j-1]
                        if(index_found[i][j+1]>0):
                            xright=index_found[i][j+1]
                        if(index_found[i+1][j]>0):
                            xdown=index_found[i+1][j]
                        x=min(xright,xleft,xdown,x)
                        index_found[i][j]=x
                        if (index_found[i][j - 1] > 0):
                            index_found[i][j - 1]=x
                        if (index_found[i][j + 1] > 0):
                            index_found[i][j + 1]=x
                        if (index_found[i + 1][j] > 0):
                            index_found[i + 1][j]=x

                elif(i==lenRow-1):#最后一行
                    if (j == 0):
                        # 第一个数据
                        if (index_found[i][j + 1] > 0):
                            xright = index_found[i][j + 1]
                        if (index_found[i - 1][j] > 0):
                            xup = index_found[i + 1][j]
                        x = min(xright, xup, x)
                        index_found[i][j] = x
                        if (index_found[i][j + 1] > 0):
                            index_found[i][j + 1]=x
                        if (index_found[i - 1][j] > 0):
                            index_found[i - 1][j]=x
                    elif (j == lenColumn - 1):
                        # 最后一排最后一列
                        if (index_found[i][j - 1] > 0):
                            xleft = index_found[i][j - 1]
                        if (index_found[i - 1][j] > 0):
                            xup = index_found[i -1][j]
                        x = min(x, xleft, xup)
                        index_found[i][j] = x
                        if (index_found[i][j - 1] > 0):
                            index_found[i][j - 1]=x
                        if (index_found[i - 1][j] > 0):
                            index_found[i -1][j]=x
                    else:
                        if (index_found[i][j - 1] > 0):
                            xleft = index_found[i][j - 1]
                        if (index_found[i][j + 1] > 0):
                            xright = index_found[i][j + 1]
                        if (index_found[i - 1][j] > 0):
                            xup = index_found[i -1][j]
                        x = min(xright, xleft, xup, x)
                        index_found[i][j] = x
                        if (index_found[i][j - 1] > 0):
                            index_found[i][j - 1]=x
                        if (index_found[i][j + 1] > 0):
                            index_found[i][j + 1]=x
                        if (index_found[i - 1][j] > 0):
                            index_found[i -1][j]=x

                else:
                    if (j == 0):
                        # 第一个数据
                        if (index_found[i][j + 1] > 0):
                            xright = index_found[i][j + 1]
                        if (index_found[i - 1][j] > 0):
                            xup = index_found[i - 1][j]
                        if(index_found[i+1][j]>0):
                            xdown=index_found[i+1][j]
                        x = min(xright, xup, x,xdown)
                        index_found[i][j] = x
                        if (index_found[i][j + 1] > 0):
                            index_found[i][j + 1]=x
                        if (index_found[i - 1][j] > 0):
                            index_found[i - 1][j]=x
                        if(index_found[i+1][j]>0):
                            index_found[i+1][j]=x

                    elif (j == lenColumn - 1):
                        # 最后一列
                        if (index_found[i][j - 1] > 0):
                            xleft = index_found[i][j - 1]
                        if (index_found[i - 1][j] > 0):
                            xup = index_found[i - 1][j]
                        if(index_found[i+1][j]>0):
                            xdown=index_found[i+1][j]
                        x = min(x, xleft, xup,xdown)
                        index_found[i][j] = x
                        if (index_found[i][j - 1] > 0):
                            index_found[i][j - 1]=x
                        if (index_found[i - 1][j] > 0):
                            index_found[i -1][j]=x
                        if(index_found[i+1][j]>0):
                            index_found[i+1][j]=x
                    else:
                        if (index_found[i][j - 1] > 0):
                            xleft = index_found[i][j - 1]
                        if (index_found[i][j + 1] > 0):
                            xright = index_found[i][j + 1]
                        if (index_found[i - 1][j] > 0):
                            xup = index_found[i - 1][j]
                        if(index_found[i+1][j]>0):
                            xdown=index_found[i+1][j]
                        x = min(xright, xleft, xup, x,xdown)
                        index_found[i][j] = x
                        if (index_found[i][j - 1] > 0):
                            index_found[i][j - 1]=x
                        if (index_found[i][j + 1] > 0):
                            index_found[i][j + 1]=x
                        if (index_found[i - 1][j] > 0):
                            index_found[i - 1][j]=x
                        if(index_found[i+1][j]>0):
                            index_found[i+1][j]=x

    maxindex=np.max(index_found)
    maxsum=0
    sumtemp=0
    for i in range(1,maxindex+1):
        sumtemp=np.sum(index_found==i)
        if(sumtemp>maxsum):
            maxsum=sumtemp
    return maxsum


def bfs_count_black(data):
    num_kind=1;
    bfs_temp=Queue();
    lenRow = data.shape[0];
    lenColumn = data.shape[1];
    index_found = np.zeros((lenRow, lenColumn), dtype=int)
    next_node=np.array([(0,1),(1,0),(0,-1),(-1,0)])
    for i in range(lenRow):
        for j in range(lenColumn):
            if(data[i][j]==1 and index_found[i][j]==0):
                bfs_temp.put([i,j]);
                num_kind=num_kind+1;
                index_found[i][j]=num_kind;
                while(not bfs_temp.empty()):
                    temp_cursor=bfs_temp.get();
                    for item in next_node:
                        if((temp_cursor[0]+item[0])<0 or (temp_cursor[0]+item[0])>lenRow-1 or (temp_cursor[1]+item[1])<0 or (temp_cursor[1]+item[1])>lenColumn-1):
                            #判断是否越界
                            continue;
                        if(data[temp_cursor[0]+item[0]][temp_cursor[1]+item[1]]==1 and index_found[temp_cursor[0]+item[0]][temp_cursor[1]+item[1]]==0):
                            #判断为黑格子且未被遍历
                            index_found[temp_cursor[0]+item[0]][temp_cursor[1]+item[1]]=num_kind;
                            bfs_temp.put(temp_cursor+item);
                        if(data[temp_cursor[0]+item[0]][temp_cursor[1]+item[1]]==0)  :
                            index_found[temp_cursor[0] + item[0]][temp_cursor[1] + item[1]] = 1;
            if(index_found[i][j]==0 and data[i][j]==0):
                index_found[i][j] = 1;
    num_kind_count=[0]*(num_kind+1);
    for i in range(lenRow):
        for j in range(lenColumn):
            num_kind_count[index_found[i][j]]=num_kind_count[index_found[i][j]]+1;
    num_kind_count=num_kind_count[2:];
    num_kind_max=max(num_kind_count);
    return num_kind_max;
if __name__ == '__main__':
    a = np.array([[0, 0, 0, 0, 1, 0, 1, 1],
                  [0, 1, 1, 0, 1, 0, 0, 0],
                  [0, 1, 0, 1, 1, 1, 0, 1],
                  [0, 0, 0, 0, 1, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1, 0, 1],
                  [0, 1, 0, 0, 1, 1, 1, 1],
                  [0, 0, 1, 1, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1]], dtype=bool)
    # print(a.shape)
    # print(a.size)
    # print(a.itemsize)
    print(count_black(a))
    print(bfs_count_black(a))

