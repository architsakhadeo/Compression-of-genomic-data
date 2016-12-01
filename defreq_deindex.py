input1 = open('pattern_list.txt','r').read().split('\n')
input2 = open('index_list.txt','r').read().split('\n')

input3 = open('huff_decoded.txt','r').read().replace('\n','')
i = 0
string = ""
t = open("decompressed.txt",'w+')
while i <= len(input3) - 1:
	#print i
	a = ""
	while not input3[i].isdigit() and i <= len(input3)-1:
		a += input3[i]
		i += 1
		if i == len(input3):
			break
	
	#print a
	string += input1[input2.index(a)]
	if i >= len(input3):
		break
	string += input3[i]
	#print string
	i += 1
	if i >= len(input3):
		break


#print string

string1 = ""
a = ""
i = 0
while i <= len(string) - 1:
	while not string[i].isdigit():
		string1 += string[i]
		i += 1 
		if i == len(string):
			break
	else:
		d = ""
		while string[i].isdigit():
			d += string[i]
			i += 1
		c = ""
		for j in range(int(d)):
			c += string[i]
		string1 += c
		i = i +1
		if i == len(string):
			break
	if i == len(string):
			break		
	
#print string1
t.write(string1)
