import re
#要想找最大独立集，应该找补图的最大团，但是把数据转化成补图的代价较大，考虑从原图入手
#发出去的边较多的点不位于独立集的可能性比较大

#首先排序
t1=[]
p=[]
f=open("CA-CondMat.txt")
line=f.readline()
L = re.split(r' ',line)
while line:
	t1.append([int(L[0]),int(L[1])])
	p.append(int(L[0]))
	line = f.readline()
	L = re.split(r' ',line)
f.close()

maxx=0
for i in t1:
	if i[0] > maxx:
		maxx = i[0]
lens = maxx+1

t2={}#记录所有点出边的次数
for i in range(lens):
	t2[i]=0
for i in p:
	t2[i] += 1

#按照每个点的出边数对字典t2降序排序,边最多的节点是t2[0][0]
t = sorted(t2.items(), key=lambda d:d[1], reverse = True)
#思路：每次都找前一个点连接的边数最多的点
def find_point(aim,choosed):
	itsp=[]
	for i in t1:
		if i[0] == aim:
			itsp.append(i[1])
			print(aim,"有边的点有：",i[1])
	m=0 
	sit=-1
	ss=[]
	for j in itsp:
		if j not in choosed:
			for k in t1:
				if k[0]==j and k[1] in choosed:#只要有边就不是独立集
					ss.append(j)
					ss = list(set(ss))
					print("当前选择的点是:",j)
					break
	for i in ss:
		if t2[i]>m and i not in unused:
			m=t2[i]
			sit=i
	if len(ss)==0:
		sit = -1
	else:
		for i in t1:
			if i[0] == aim or i[1]==aim:
				t1.remove(i)
	print("当前选入不属于独立集的集合的点是:",sit)
	return sit

choosed=[]
unused=[]
choosed.append(t[0][0])
first = find_point(t[0][0],choosed)
for ss in range(lens):
	choosed.append(first)
	choosed=list(set(choosed))
	first = find_point(first,choosed)
	if first == -1:
		res=lens-len(choosed)
		break
	print("当前选择的点：",first)


print("总共有",lens,"个点，最大独立集点的个数为：",res)




