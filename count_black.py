import numpy as np
import sys
a=np.array([[0,0,0,0,1,0,1,1],
            [0,1,1,0,1,0,0,0],
            [0,1,0,1,1,1,0,1],
            [0,0,0,0,1,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,1,0,0,1,1,1,1],
            [0,0,1,1,0,1,0,0],
            [0,0,0,1,0,1,0,1]],dtype=bool)
print(a.shape)
print(a.size)
print(a.itemsize)

def count_black(data):
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

print(count_black(a))
