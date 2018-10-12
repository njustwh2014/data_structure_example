import numpy as np
import time
from queue import Queue

class state_node:#记录状态节点
    def __init__(self,dot,parentdot):
        self.dot=dot
        self.parentdot=parentdot
        self.isroot=False

def node_operate(si,sj):
    a=Queue()
    if((si<0)or(si>N-1)or(sj<0)or(sj>N-1)):
        return a
    else:
        state_node_temp = []
        for i in range(8):
            state_node_temp.append(state_node((0, 0), (si, sj)))
        for i in range(8):
            state_node_temp[i].dot=(si+direction[i][0],sj+direction[i][1])
            a.put(state_node_temp[i])
        return a

def knight_der_find(si,sj,di,dj):
    steps=0
    solution=[]
    flag_node=True
    temp=(0,0)
    dst=(di,dj)
    node_temp=(0,0)
    current_layer=Queue()
    next_layer=Queue()
    next_layer_temp=Queue()
    initnode=state_node((si,sj),(si,sj))
    initnode.isroot=True
    current_layer.put(initnode)
    closelist=[]
    closelist.append(initnode)
    while(steps<N*N):#bfs
        while(not current_layer.empty()):
            temp = current_layer.get()
            if ((temp.dot[0] < 0) or (temp.dot[0] > N - 1) or (temp.dot[1] < 0) or (temp.dot[1] > N - 1)):
                continue;
            else:
                if (dst == temp.dot):
                    solution.append(temp)
                    while(not temp.isroot):
                        for node in closelist:
                            if(node.dot==temp.parentdot):
                                temp=node
                                break
                        solution.append(temp)
                    return steps,solution;
                else:
                    next_layer_temp=node_operate(temp.dot[0],temp.dot[1])
                    while(not next_layer_temp.empty()):
                        flag_node=True
                        node_temp=next_layer_temp.get()
                        for node in closelist:
                            if(node.dot==node_temp.dot):
                                flag_node=False
                                break
                        if(flag_node):
                            next_layer.put(node_temp)
                            closelist.append(node_temp)
        steps=steps+1;
        while(not next_layer.empty()):
            temp=next_layer.get()
            current_layer.put(temp)

    return steps,solution;

if __name__=='__main__':
    starttime = time.clock()
    N = 30;  # 棋盘大小
    SI = 0;
    SJ = 0;  # 初始位置
    DI=25;
    DJ=25;#目标位置
    STEPS = N * N - 1;
    steps_min=0
    solution_min_step=0
    solution_min=[]
    solution_min_temp=state_node((0,0),(0,0))
    direction = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    chess_map = np.zeros((N, N), dtype=int)
    steps_min,solution_min=knight_der_find(SI,SJ,DI,DJ)
    print("min steps:",steps_min)
    while(len(solution_min)):
        solution_min_temp=solution_min.pop()
        solution_min_step=solution_min_step+1
        chess_map[solution_min_temp.dot[0]][solution_min_temp.dot[1]]=solution_min_step
    print(chess_map)
    endtime = time.clock()
    print("Total running time: %s s" % (str(endtime - starttime)))