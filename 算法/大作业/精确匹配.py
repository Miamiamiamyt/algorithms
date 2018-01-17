#根据存入本地的索引生成精确匹配
#注意OCC是每隔16个存一个，最后一个可能超出了字符串的长度，先找到最近的位置再精确匹配
import re
import math
import datetime

def FM_Reduction(line):#还原FM-index
	suffix_array = re.split(r' ',line)
	#print(suffix_array[0])
	suffix_array.remove('\n')
	print(len(suffix_array))
	#suffix_array.remove('')
	return suffix_array

def C_Reduction(line):#还原C
	C={}
	temp = re.split(r' ',line)
	i=0
	while i<len(temp)-1:
		C[temp[i]]=int(temp[i+1])
		i += 2
	temp.clear()
	return C
def OCC_Reduction(line):#还原OCC
	OCC={}
	temp = re.split(r' ',line)
	length = 2*int(300000/16) #37500
	#print(length)
	i = 0
	while i<len(temp)-1:
		OCC[temp[i]]={}
		#print(temp[i])
		j=i
		i += 1
		while i<=j+length:
			OCC[temp[j]][int(temp[i])]=int(temp[i+1])
			i += 2
		i = j+length
		i += 1
	temp.clear()
	return OCC
def PRECISION(beg,sit,C,suffix_array,ff,aim):#根据最近的位置来计算精确的OCC
	f = open(r"s.txt")
	f.read(10)
	f.seek((ff-1)*100000,1)
	S = f.read(300000)
	f.close()
	L=[]
	for i in suffix_array:#取出的suffix是str类的
		if i is not '\n':
			L.append(S[int(i)-1])
	#print(F,L)	
	res = -1
	print("PRECISION-beg",beg)
	for i in range(beg,sit):
		if L[i]==aim:
			res=i#找到第一个即可
			break
	print("PRECISION-res",res)
	count = 0
	for i in range(0,res):#求在他之前有几个他
		if L[i] == aim:
			count += 1 
	count = C[aim]+count
	print("PRECISION",aim,count)
	return count,L[count]

def Match_Second(res,ff,cur,S,R,suffix_array,C):
	f = open(r"s.txt")
	f.read(10)
	f.seek((ff-1)*100000,1)
	SS = f.read(300000)
	f.close()
	aim = S[cur]
	L=[]
	R.append(aim)
	for i in suffix_array:#取出的suffix是str类的
		L.append(SS[int(i)-1])
	#print(F,L)	
	count = 0
	for i in range(0,res):#求在他之前有几个他
		if L[i] == aim:
			count += 1 
	print(res,aim,cur,count,C[aim])
	#print(aim,count)
	L.clear()
	#print(aim,res,cur)
	count = C[aim]+count
	print(count)
	print("当前位置",count,suffix_array[count])
	if cur == 0:
		print("该子串取自原长串的第",suffix_array[count],"位置")
		return
	Match_Second(count,ff,cur-1,S,R,suffix_array,C)


def Match_First(S,C,OCC,suffix_array,ff):#匹配
	R=[]
	cur = len(S)-1
	#print(S[0])
	rangea=[0,C['C']]
	rangec=[C['C'],C['G']]
	rangeg=[C['G'],C['T']]
	ranget=[C['T'],300000]
	r = []
	if S[cur] == 'A':
		r = rangea
	elif S[cur] == 'C':
		r = rangec
	elif S[cur] == 'G':
		r = rangeg
	elif S[cur] == 'T':
		r = ranget
	flag = False #判断是否匹配成功的指示变量
	i=0
	while i < r[1]:
		if i == 0:
			sit = math.ceil((i+1)/16)*16
		else:
			sit = math.ceil(i/16)*16
		i=i+17
		if OCC[S[cur-1]][sit]>0:#要进一步精确
			print("sit",S[cur-1],sit,OCC[S[cur-1]][sit])
			beg = sit-16
			while beg < sit:
				print("beg",beg,"cur",cur)
				res,judge=PRECISION(beg,sit,C,suffix_array,ff,S[cur-1])
				if res == -1:
					continue
				if(judge==S[cur-2]):
					Match_Second(res,ff,cur-2,S,R,suffix_array,C)
					R.reverse()
					R.append(S[198])
					R.append(S[199])
					#print(R)
					R=''.join(R)
					if R == S:
						print("匹配成功")
						print(R)
						return
					else:
						beg += 1
						print(R)
						R=[]
				else:
					beg += 1
	return

			
def main():
	#S一行200个
	S = 'TGCAATTTCTACTATAGTTACTCATTAAGTTATCTAGTAAATTACCATGTAATGTATAAGCTGTGGAATTAATTCTCAGTTACATAGCATTCACCATGTAATTACTAAACAGTCCCCATCATTACAGCTTTCTAGCCTATTATGAAAAGACCAGAAACATAATTTCAATTACAAAGCCCCTGTTGGAACCGAAAGGGTTT'
	ff=1
	filename=str(ff)+".txt"
	f = open(filename,"r")
	line = f.readline()
	suffix_array = FM_Reduction(line)
	for i in range(len(suffix_array)):
		if int(suffix_array[i]) == 0:
			print(i)
	line = f.readline()
	C = C_Reduction(line)
	line = f.readline()
	OCC=OCC_Reduction(line)
	f.close()
	Match_First(S,C,OCC,suffix_array,ff)
	

if __name__ == "__main__":
	start = datetime.datetime.now()
	main()
	end = datetime.datetime.now()
	print (end-start)

