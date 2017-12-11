import re
f = open("data8.dat")
line = f.readline()
L = re.split(r', ',line)
spot = []
while line:
	line = f.readline()
	spot.append(line)

#贪心算法，并且数据已经排序好
def best_addwater(spot,N=int(L[0]),m=int(L[1]),k=int(L[2])):
	begin = 0
	#now = 0
	c = 0
	result = []
	while begin <= N and c < k:
		if int(spot[c])-begin == m:
			result.append(int(spot[c]))
			begin = int(spot[c])
		elif int(spot[c])-begin > m:
			result.append(int(spot[c-1]))
			begin = int(spot[c-1])
		c = c + 1
	return result

def main():
   res = best_addwater(spot);
   count = 0
   for i in res:
   	count = count + 1
   	print(i)
   print("共补水%d次"%count)

if __name__=="__main__":
    main()
