#思路是递归遍历和启发式优化
import numpy as np
import time
import sys
def knight_traveled_around(si,sj,steps):
    #初始化下一个节点数组，每个元素的第三个数字表示下一步优先递归的权重
    Next_Node = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
    x_temp=0
    if(chess_map[si][sj]!=0):
        return False;
    if(steps==0):
        #表示成功遍历了一次
        steps=steps-1;
        chess_map[si][sj] = STEPS - steps;
        return True;
    steps = steps - 1;
    chess_map[si][sj]=STEPS-steps;#存储步骤数
    for i in range(8):
        Next_Node[i]=(si+direction[i][0],sj+direction[i][1],0)
        #首先判断节点是否在棋盘内
        if ((Next_Node[i][0] < 0) or (Next_Node[i][0] > N-1) or (Next_Node[i][1]<0) or (Next_Node[i][1]>N-1) ):
            Next_Node[i] = (Next_Node[i][0], Next_Node[i][1], sys.maxsize)
        else:
            #启发式优化，优先递归遍历靠近棋盘边缘
            x_temp = min(Next_Node[i][0], N - 1 - Next_Node[i][0]) + min(Next_Node[i][1], N - 1 - Next_Node[i][1])
            Next_Node[i] = (Next_Node[i][0], Next_Node[i][1], x_temp)
    Next_Node.sort(key=lambda x:x[2])
    for i in range(8):
        if(Next_Node[i][2]<N):
            if (knight_traveled_around(Next_Node[i][0], Next_Node[i][1], steps) == True):
                return True;
    chess_map[si][sj]=0;#遍历失败，往后退一步
    return False;









if __name__=='__main__':
    starttime = time.clock()
    N =10;  # 棋盘大小
    SI = 0;
    SJ = 0;  # 初始位置
    STEPS = N * N - 1;
    direction=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

    chess_map = np.zeros((N,N),dtype=int)

    if(knight_traveled_around(SI,SJ,STEPS)==True):
        print(chess_map)
    else:
        print("Sorry, I can not find the solution")
    endtime = time.clock()
    print("Total running time: %s s" % (str(endtime - starttime)))
