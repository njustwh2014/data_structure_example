#思路是基于深度优先搜索暴力求解
#实现字符串中两个位置的字符互换
def switchchar(str,p1,p2):
    #确保p1是左标号
    left=p1
    right=p2
    if(p1>p2):
        left=p2
        right=p1
    elif(p1==p2):
        return str
    lstr=""
    rstr=""
    mstr=""
    if(left==0):
        lstr=""
    else:
        lstr=str[:left]
    if(right==len(str)-1):
        rstr=""
    else:
        rstr=str[right+1:]
    if((right-left)==1):
        mstr=""
    else:
        mstr=str[left+1:right]
    return lstr+str[right]+mstr+str[left]+rstr

#用对象表示状态点
class StateNode:
    def __init__(self,value,dstvalue,step):
        self.value=value
        self.index=value.find("*")
        self.assess=0
        self.dstvalue=dstvalue
        if(self.index<0):
            print(self.tostring()+"error")
            raise RuntimeError
        for i in range(len(value)):
            if(value[i]==dstvalue[i]):
                self.assess += 1
        self.step=step

    def tostring(self):
            return "Node:{0} assess={1} step={4}\n     {2}\n     {3}\n".format(self.value[:3], self.assess,
                                                                               self.value[3:6], self.value[6:],
                                                                               self.step)

    def left(self):
        if(self.index % 3 != 0):
            return StateNode(switchchar(self.value, self.index - 1, self.index), self.dstvalue, self.step + 1)

    def right(self):
        if(self.index % 3 != 2):
            return StateNode(switchchar(self.value, self.index + 1, self.index), self.dstvalue, self.step + 1)

    def up(self):
        if(self.index > 2):
            return StateNode(switchchar(self.value, self.index - 3, self.index), self.dstvalue, self.step + 1)

    def down(self):
        if(self.index < 6):
            return StateNode(switchchar(self.value, self.index + 3, self.index), self.dstvalue, self.step + 1)

def calc(startval,endval):
    startNode=StateNode(startval,endval,0)
    openlist=[startNode]
    closelist=[]
    while True:
        #评估，使用assess值
        openlist=sorted(openlist,key=lambda node:node.assess)
        curNode=openlist.pop()
        if(curNode==None):
            print("End")
            return

        print(curNode.tostring())

        if(curNode.assess==9):
            print("Found,End!")
            return

        leftNode=curNode.left()
        rightNode=curNode.right()
        upNode=curNode.up()
        downNode=curNode.down()

        if(leftNode!=None):
            exist=False
            for node in openlist:
                if(leftNode.value==node.value):
                    exist=True
                    break
            for node in closelist:
                if(leftNode.value==node.value):
                    exist=True
                    break
            if(not exist):
                openlist.append(leftNode)

        if (rightNode != None):
            exist = False
            for node in openlist:
                if (rightNode.value == node.value):
                    exist = True
                    break
            for node in closelist:
                if (rightNode.value == node.value):
                    exist = True
                    break
            if (not exist):
                openlist.append(rightNode)

        if (upNode != None):
            exist = False
            for node in openlist:
                if (upNode.value == node.value):
                    exist = True
                    break
            for node in closelist:
                if (upNode.value == node.value):
                    exist = True
                    break
            if (not exist):
                openlist.append(upNode)

        if (downNode != None):
            exist = False
            for node in openlist:
                if (downNode.value == node.value):
                    exist = True
                    break
            for node in closelist:
                if (downNode.value == node.value):
                    exist = True
                    break
            if (not exist):
                openlist.append(downNode)

        closelist.append(curNode)

if __name__=='__main__':
    calc("123*45678","1*2345678")