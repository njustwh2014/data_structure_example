import numpy as np
# 用Kruskal算法实现最小生成树
#建立并查集 搜索Find 合并连通域Union
class MST():
    def __init__(self,edges=np.array([]),n=0,m=0):
        self.edges=edges;#无向图边的信息 格式：u v w u和v是顶点编号，从1开始，w是边的权重。
        self.n=n;#无向图的顶点数
        self.m=m;#无向图的边数
        self.parent=[-1]*(n+1);#建立每个顶点所在连通域的根节点
        self.edges=self.edges[np.lexsort(self.edges.T)];
        self.mst=np.array([]);
    def __find__(self,x):
        s=x;
        while(s>=0 and self.parent[s]>=0):
            s=self.parent[s];
        while(s!=x):#压缩搜索路径
            temp=self.parent[x];
            self.parent[x]=s;
            x=temp;
        return s;

    def __union__(self,N1,N2):#合并两个节点所在的连通域
        r1=self.__find__(N1);
        r2=self.__find__(N2);
        temp=self.parent[r1]+self.parent[r2];
        if(self.parent[r1]>self.parent[r2]):
            self.parent[r2]=r1;
            self.parent[r1]=temp;
        else:
            self.parent[r1]=r2;
            self.parent[r2]=temp;

    def kruskal(self):
        sumweight=0;
        num=0;
        for item in self.edges:
            if(self.__find__(item[0])!=self.__find__(item[1])):
                sumweight=sumweight+item[2];
                num=num+1;
                if(num==1):
                    self.mst=np.array([item]);
                else:
                    self.__union__(item[0], item[1]);
                    item_x=np.array(item);
                    self.mst=np.insert(self.mst,0,values=item_x,axis=0);
            if(num>self.n-1):
                break
        return self.mst,sumweight;










if __name__ == '__main__':
    graph_edges=np.array([[1,2,6],[1,3,1],[1,4,5],[2,3,5],[2,5,3],[3,4,5],[3,5,6],[3,6,4],[4,6,2],[5,6,6]]);
    graph_edges=graph_edges[np.lexsort(graph_edges.T)];
    graph_node_num=6;
    graph_edges_num=9;
    MST_1=MST(graph_edges,graph_node_num,graph_edges_num);
    mst,weight=MST_1.kruskal();
    print(mst);
    print(weight);

