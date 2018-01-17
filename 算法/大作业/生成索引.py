import os
#python的sorted函数直接能够实现将字符串按照字典序排序
def Move_To_Right(S):
	SS=S#记录初始状态
	#result=[]
	#result.append(SS)
	result={}
	result[SS]=0
	#suffix_array.append(0)
	for j in range(len(SS)-1):
		temp = SS[0]
		SS = SS[1:] + temp
		#result.append(SS)
		#suffix_array.append(j+1)
		result[SS]=j+1
	return result

#同时也要注意空间复杂度
#一开始想的是根据results修改suffix_array，时间复杂度较大
def BWT():
	suffix_array=[]
	results = []
	result = Move_To_Right(S)
	results = sorted(result.keys())#但是要根据results修改suffix_array
	for i in results:
		suffix_array.append(result[i])
	#print(results,suffix_array)
	result.clear()
	results.clear()
	return suffix_array

#不生成矩阵创建索引
def exchange(A,a,b):
	temp = A[a]
	A[a]=A[b]
	A[b]=temp
def QUICKSORT(S,suffix_array,p,r):
	if p<r:
		q=PARTITION(S,suffix_array,p,r)
		QUICKSORT(S,suffix_array,p,q-1)
		QUICKSORT(S,suffix_array,q+1,r)

def PARTITION(S,suffix_array,p,r):
	n=len(suffix_array)
	x=suffix_array[r]
	i=p-1
	for j in range(p,r):
		if S[suffix_array[j]:suffix_array[j]+n-1]<S[x:x+n-1]:
			i = i+1
			exchange(suffix_array,i,j)
	exchange(suffix_array,i+1,r)
	return i+1

def BWT1(SS):
	suffix_array=[] 
	for i in range(int(len(SS)/2)):
		suffix_array.append(i)
	QUICKSORT(SS,suffix_array,0,len(suffix_array)-1)
	print("FM-index:",suffix_array)
	return suffix_array



#建立C和OCC数组——当前想法有两层循环
#根据suffix_array就可以得到F和L
#默认只有AGCT四种字符
def Build_Structure(S):
	SS = S+S
	F=[]
	L=[]
	suffix_array=[]
	suffix_array=BWT1(SS)
	for i in suffix_array:
		F.append(S[i])
		L.append(S[i-1])
	#print(F,L)	
	C={}#C表示的是在第一列的字符串,比字符X小的有多少个
	OCC={}#OCC的的元素OCC[X][i]表示的意思是在最后一列字符串中,前i个字符里有几个字符X
	#首先求C
	counta=0#记录agct个数
	countg=0
	countc=0
	#countt=0
	for i in F:
		if i == 'A':
			counta += 1
		elif i == 'C':
			countc += 1
		elif i == 'G':
			countg += 1
	C['A']=0
	C['C']=counta
	C['G']=counta+countc
	C['T']=counta+countc+countg
	#接下来求OCC
	OCC['A']={}
	OCC['G']={}
	OCC['C']={}
	OCC['T']={}
	i=0
	counta=0#记录agct个数
	countg=0
	countc=0
	countt=0
	while i < len(L):
		#i=i+16
		for j in L[i:i+16]:
			if j=='A':
				counta += 1
			elif j=='G':
				countg += 1
			elif j=='C':
				countc += 1
			elif j=='T':
				countt += 1
		i=i+16
		OCC['A'][i]=counta
		OCC['G'][i]=countg
		OCC['C'][i]=countc
		OCC['T'][i]=countt	
	F.clear()
	L.clear()
	return suffix_array,C,OCC
def main():
	file = open('s.txt','r')
	file.read(10)#前面10个是记录长度的和制表符
	begin=100010
	ff=1
	S=file.read(300000)
	while S:
		file.seek(begin,0)
		begin += 100000
		print(S)
		if str(0xFF) in S:
			S.remove(str(0xFF))
		suffix_array,C,OCC=Build_Structure(S)
		filename = str(ff)+'.txt'
		f = open(filename,'w')
		for i in suffix_array:
			f.write(str(i)+' ')
		f.write('\n')
		for i in C:
			f.write(i+' '+str(C[i])+' ')
		f.write('\n')
		for i in OCC:
			f.write(i+' ')
			for j in OCC[i]:
				f.write(str(j)+' '+str(OCC[i][j])+' ')
		f.write('\n')
		ff += 1
		f.close()
		S=file.read(300000)
	file.close()


if __name__ == "__main__":
	main()

