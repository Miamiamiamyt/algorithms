# 1.py与2.py都用的是书上的例子作为测试
#利用字典来存储图
#用优先队列太麻烦了，其实就是选择与当前结点距离最小的点
# Dijkstra算法——通过边实现松弛
# 指定一个点到其他各顶点的路径——单源最短路径

# 初始化图参数
# 源节点为s
G = {'s':{'t':10,'y':5},
	't':{'y':2,'x':1},
	'y':{'t':3,'x':9,'z':2},
	'x':{'z':4},
	'z':{'s':7,'x':6}
	}
#在python中INITIALIZE-SINGLE-SOURCE函数可以省略，利用字典直接赋值,用65535表示正无穷
d = {'s':0,
	't':65535,
	'y':65535,
	'x':65535,
	'z':65535
	}
#因此不需要使用优先队列就可以找到当前d值最小的结点
def FIND_MinD(d,V):
	minp = 65535
	for i in V:
		if d[i]<minp:
			minp = d[i]
			res = i
	return res
# dijkstra算法
def Dijkstra(G,d):
	#首先得到结点集
	V=[]
	for i in G.keys():
		V.append(i)
	s=[]
	pi = {'s':'','t':'','y':'','x':'','z':''}
	while V:
		u = FIND_MinD(d,V)
		s.append(u)
		V.remove(u)
		for v in G[u].keys():
			if d[v]>d[u]+G[u][v]:
				d[v]=d[u]+G[u][v]
				pi[v]=u
	return pi

aim = input("请输入您想到达的结点:\n")
aim1 = aim
pi=Dijkstra(G,d)
res=[]
while aim != '':
	res.append(aim)
	aim=pi[aim]
res.reverse()
for i in res:
	if i == aim1:
		print(i)
	else:
		print(i,end="->")
	





