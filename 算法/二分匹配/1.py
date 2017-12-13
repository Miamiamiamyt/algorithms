import copy
#最大二分匹配的输入应该是L与R，L与R的并集组成边集
#利用dist来存图

L={'a':'f','b':'h','c':'g','d':'h','e':'h'}
R={'f':'b','g':'c','h':'c','i':'c'}

#首先将二分图转化为有向流图,每条边的容量都为1
def trans(L,R):
	G={}
	#set用update
	r={}
	for i in R.keys():
		temp={}
		r.setdefault(i,0)
		temp.setdefault('t',1)
		temp.setdefault(R[i],0)
		for j in L.keys():
			if L[j]==i:
				temp.setdefault(j,0)
		G[i]=temp
	G['t']=r

	l={}
	for i in L.keys():
		temp={}
		l.setdefault(i,1)
		temp.setdefault('s',0)
		temp.setdefault(L[i],1)
		for j in R.keys():
			if R[j]==i:
				temp.setdefault(j,1)
		G[i]=temp
	G['s']=l
	return G

#判断s到t的简单路径,利用二分图的性质，简单路径只会是s->u~>v->t
def has_path(G,u,path,visited):
	Gf=copy.deepcopy(G)
	for i in Gf[u].keys():
		if Gf[u][i]==1 and i != 's' :
			if Gf[i]['t']==1:
				#print(u,i)
				path.append(i)
				visited.append({u,i})
				#print("mm",path)
				return True
			else:
				for j in Gf[i].keys():
					if Gf[i][j]==1 and {i,j} not in visited:
						print(u,i,j)
						path.append(i)
						path.append(j)
						visited.append(i,j)
						if has_path(Gf,j,path,visited)==False:
							path.remove(i)
							path.remove(j)
							visited.remove({i,j})
							return False
						else:
							return True
						#print("mmm",u,path)								
	return False


#FORD_FULKERSON
def FORD_FULKERSON(L,R):
	Gf=trans(L,R)
	visited = []
	for i in L.keys():
		path = []
		if has_path(Gf,i,path,visited) and Gf['s'][i]==1:
			#print(i,path)
			Gf['s'][i]=0
			Gf[i]['s']=1
			temp = i
			for j in path:
				if temp in L.keys():
					Gf[temp][j]=0
					Gf[j][temp]=1
				else:
					Gf[temp][j]=1
					Gf[j][temp]=0
				temp=j
			Gf[j]['t']=0
			Gf['t'][j]=1
	res = 0  
	for r in Gf['t']:
		res = res + Gf['t'][r]
	print(Gf)
	return res

res=FORD_FULKERSON(L,R)
print("有",res,"个匹配")









