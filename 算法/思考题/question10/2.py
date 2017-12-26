class node(object):
	def __init__(self,name):
		self.p=None
		self.rank=0
		self.name=name


def MAKE_SET(x):
	x.p=x
	x.rank=0

def FIND_SET(x):#带路径压缩
	if x is not x.p:
		x.p=FIND_SET(x.p)
	return x.p

def LINK(x,y):#按秩合并
	if x.rank > y.rank:
		y.p=x
	else:
		x.p=y
		if x.rank == y.rank:
			y.rank += 1

def UNION(x,y):
	LINK(FIND_SET(x),FIND_SET(y))

def FIND_MIN(G,choosed):#找到一个图中权重最小的边
	mmin=100 #暂时用100来表示一个较大的数
	e1=None
	E2=None
	for i in G.keys():
		for j in G[i].keys():
			if G[i][j] < mmin and [i,j] not in choosed:
				mmin = G[i][j]
				e1 = i
				e2 = j
	return e1,e2

def END_POINT(choosed):
	V = []
	for i in choosed:
		for v in i:
			V.append(v)
	V=list(set(V))
	return V

def MST_KRUSKAL(G):
	A=[]
	choosed=[]#记录被判断过的边
	V=[]
	#首先得到顶点集
	for i in G.keys():
		V.append(i)
		for j in G[i].keys():
			V.append(j)
	V=list(set(V))
	for v in V:
		MAKE_SET(v)
	while len(END_POINT(choosed)) != len(V):#最小生成树还没有形成
	    u,v = FIND_MIN(G,choosed)
	    print(u.name,FIND_SET(u).name,v.name,FIND_SET(v).name)
	    if FIND_SET(u) != FIND_SET(v):
	    	A.append([u.name,v.name])
	    	UNION(u,v)
	    choosed.append([u,v])
	    choosed.append([v,u])
	return A



a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')
g = node('g')
h = node('h')
i = node('i')
G = {a:{b:4,h:8},
    b:{a:4,h:11,c:8},
    c:{b:8,i:2,f:4,d:7},
    d:{c:7,f:14,e:9},
    e:{d:9,f:10},
    f:{e:10,d:14,c:4,g:2},
    g:{f:2,i:6,h:1},
    h:{g:1,i:7,b:11,a:8},
    i:{c:2,g:6,h:7}}
print(MST_KRUSKAL(G))