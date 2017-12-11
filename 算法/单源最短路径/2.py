# 与1.py同理
# Bellman-Ford算法允许有负权边，但不允许有负环

# 首先规定图
G={'s':{'t':6,'y':7},
	't':{'x':5,'y':8,'z':-4},
	'y':{'x':-3,'z':9},
	'x':{'t':-2},
	'z':{'s':2,'x':7}
}
# 规定各结点的d，即INITIALIZE-SINGLE-SOURCE函数
d={'s':0,'t':65535,'y':65535,'x':65535,'z':65535}

# Relax函数
pi = {'s':'','t':'','y':'','x':'','z':''}
def Relax(G,u,v):
	if d[v]>d[u]+G[u][v]:
		d[v]=d[u]+G[u][v]
		pi[v]=u

def BELLMAN_FORD(G,d):
	#首先得到结点集
	V=[]
	for i in G.keys():
		V.append(i)
	for i in range(1,len(V)):
		for u in G.keys():
			for v in G[u].keys():
				Relax(G,u,v)

	for u in G.keys():
		for v in G[u].keys():
			if d[v]>d[u]+G[u][v]:
				return False
	return True

aim = input("请输入您想到达的结点:\n")
aim1 = aim
r=BELLMAN_FORD(G,d)
res=[]
if r ==True:
	while aim != '':
		res.append(aim)
		aim=pi[aim]
	res.reverse()
	for i in res:
		if i == aim1:
			print(i)
		else:
			print(i,end="->")
else:
	print("有负环路，失败")



