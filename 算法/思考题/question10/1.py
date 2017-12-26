import math
class node(object):
	def __init__(self,name,key):
		self.name=name
		self.p=None
		self.child=None
		self.degree=0
		self.right=None
		self.left=None
		self.mark=False
		self.key=key

class FibHeap(object):
	def __init__(self):
		self.n=0
		self.min=None

	def FIB_HEAP_INSERT(self,node):
		if self.min==None:
			self._listInit(node)
			self.min=node
		else:
			self._listInsert(self.min,node)
			if node.key < self.min.key:
				self.min=node
		self.n=self.n+1

	#根链表是环形双向链表
	def FIB_HEAP_UNION(self,heap):
		self._listUnion(self.min,heap.min)
		if self.min > heap.min:
			self.min = heap.min
		self.n = self.n + heap.n

	def FIB_HEAP_EXTRACT_MIN(self):
		z=self.min
		if z != None:
			self._removeParent(z.child)
		self._listRemove(z)
		if z==z.right:
			self.min = None
		else:
			self.min = z.right
			self._CONSOLIDATE()
		self.n = self.n - 1
		return z

	def addChild(self, parent, child): 
		if parent.child == None: 
			parent.child = child 
			self._listInit(child) 
		else: 
			self._listInsert(parent.child, child) 
		child.p = parent 
		child.mark = False 
		parent.degree += 1
		self.n += 1 

	def FIB_HEAP_DECREASE_KEY(self,x,k):
		if k>x.key:
			print("error")
			return
		x.key = k
		y = x.p
		if y and x.key<y.key:#要调整堆了
			self._CUT(x,y)
			self._CASCADING_CUT(y)
		if x.key < self.min.key:
			self.min = x

	def _CUT(self,x,y):
		self._removeChild(y,x)
		self._listInsert(self.min,x)
		x.mark=False

	def _CASCADING_CUT(self,y):
		z=y.p
		if z:
			if y.mark == False:
				y.mark=True
			else:
				self._CUT(y,z)
				self._CASCADING_CUT(z)


	def _removeChild(self,parent,child,Flag=True):
		c = parent.child
		if c == child:
			if child.right != child:
				parent.child = child.right
				self._listRemove(child)
			else:
				parent.child = None
		else:
			self._listRemove(child)
		max = -1
		while Flag:
			max = c.degree
			if c.right == c:
				Flag=False
			c=c.right
			if c.degree > max:
				max = c.degree			 
		parent.degree=max+1
		child.p=None

	def _removeParent(self,child):
		if child:
			t = child.key 
			temp = child.right
			child.p=None
			#temp = child
			self._listInsert(self.min,child)
			child=temp
			while child.key != t:
				temp=child.right
				child.p=None
				self._listInsert(self.min,child)
				child = temp

	def _listInsert(self,head,node):
		node.left = head 
		node.right = head.right 
		node.right.left = node 
		head.right = node

	def _listInit(self,head): 
		head.left = head.right = head

	def _listUnion(self,node1,node2):
		temp1 = node1.right
		temp2 = node2.left
		node1.right = node2
		node2.left = node1
		temp2.right = temp1
		temp1.left = temp2

	def _listRemove(self,z):#有根链表只有一个结点的情况
		temp1=z.left
		temp2=z.right
		temp1.right=temp2
		temp2.left=temp1

	

	def _exchange(self,x,y):
		temp = x
		x = y
		y = temp


	def _CONSOLIDATE(self,islist=True):
		A = []
		for i in range(int(math.log2(self.n))+2):
			A.append(None)
		temp = []
		x = self.min
		while islist:
			if x.right.right in temp:
				break
			temp.append(x)
			d=x.degree
			if A[d] != None:
				#print(A[d].key)
				y = A[d]
				if x.key > y.key:
					self._exchange(x,y)
				self._FIB_HEAP_LINK(y,x)
				A[d]=None
				d=d+1
			A[d]=x
			#print(d,x.name)
			x=x.right
		self.min=None
		for i in range(int(math.log2(self.n))+1):
			if A[i] != None:
				#print(A[i].key)
				if self.min == None:
					self._listInit(A[i])
					self.min=A[i]
				else:
					self._listInsert(self.min,A[i])
					if A[i].key < self.min.key:
						self.min=A[i]

	def _FIB_HEAP_LINK(self,y,x):
		self._listRemove(y)
		self.addChild(x,y)
		y.mark = False

#将图转化为斐波那契堆实现的优先队列,由于key值都较小，所以用100代替正无穷：
Q=FibHeap()
a=node('a',0)
b=node('b',100)
c=node('c',100)
d=node('d',100)
e=node('e',100)
f=node('f',100)
g=node('g',100)
h=node('h',100)
i=node('i',100)
#需要dist来记录pi和w
w={a:{b:4,h:8},
   b:{a:4,h:11,c:8},
   c:{b:8,i:2,f:4,d:7},
   d:{c:7,f:14,e:9},
   e:{d:9,f:10},
   f:{e:10,d:14,c:4,g:2},
   g:{f:2,i:6,h:1},
   h:{g:1,i:7,b:11,a:8},
   i:{c:2,g:6,h:7}}
pi={a:None,b:None,c:None,d:None,e:None,f:None,g:None,h:None,i:None}

Q.FIB_HEAP_INSERT(a)
Q.FIB_HEAP_INSERT(b)
Q.FIB_HEAP_INSERT(c)
Q.FIB_HEAP_INSERT(d)
Q.FIB_HEAP_INSERT(e)
Q.FIB_HEAP_INSERT(f)
Q.FIB_HEAP_INSERT(g)
Q.FIB_HEAP_INSERT(h)
Q.FIB_HEAP_INSERT(i)

def MST_PRIM(Q,w,pi):
	choosed=[]
	while Q:
		u=Q.FIB_HEAP_EXTRACT_MIN()
		#print(Q.min.name)
		choosed.append(u)
		for v in w[u]:
			if v not in choosed and w[u][v]<v.key:
				pi[v]=u
				Q.FIB_HEAP_DECREASE_KEY(v,w[u][v])
				print(v.name,v.key)
MST_PRIM(Q,w,pi)
print(pi)




