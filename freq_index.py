import time
input = open('input_file.txt','r').read().replace('\n','')
aa = open('Jude.txt','w+')
aa.write(input)
x = open('midfile.txt','w+')
y = open('midmidfile.txt','w+')
z = open('ordered.txt','w+')
q = open('capital.txt','w+')
start = time.time()
output = ""
i = 0
import time
start = time.time()
while i < len(input):
	count = 0
	print i
	for j in range(i,len(input)):
		if input[i] == input[j]:
			count += 1
		else:
			break
	if count <= 2:
		for l in range(count):
			output += input[l + i]
	else:
		output += str(count)
		output += input[i]
	i = i + count
#print time.time() - start
y.write(output)
print "Original data ",len(input) 
print "Compressed data ",len(output)
print "Compression ratio ",float(len(input))/len(output)


inputfile2 = output
outputfile2 = open('output_file3.txt','w+')
output2 = ""
for i in range(len(inputfile2)):
	c = ""
	if inputfile2[i].isdigit():
		c = " "
	else:
		c = inputfile2[i]
	output2 += c

output3 = output2.split()
for i in output3:
	x.write(i + ' ')
	
from collections import defaultdict
frequency = defaultdict(int)
for symbol in output3:
	frequency[symbol] += 1
print len(frequency)
from collections import OrderedDict
ordered = sorted(OrderedDict(frequency),key=frequency.get,reverse=True)
for i in ordered:
	z.write(i + '\n')

capital = [chr(ord('a')+i) for i in range(26)]
i = 0
count = 26
flag = 0
seed = ""
while True:
	seed = capital[i]
	for j in range(26):
		seed2 = seed
		seed2 += capital[j]
		capital.append(seed2)
		count += 1
		if count >= len(ordered):
			flag = 1
			break
	i += 1
	if flag == 1:	
		break
print capital
for i in capital:
	q.write(i + '\n')


final = ""
i = 0
while i < len(inputfile2):
	c = ""	
	if inputfile2[i].isdigit():
		c += inputfile2[i]
		final += c
		i += 1
		continue
	else:
		while i < len(inputfile2) and not inputfile2[i].isdigit():
						
			c += inputfile2[i]
			i += 1
		if c in ordered:
			final += capital[ordered.index(c)]

outputfile2.write(final)
#print time.time() - start
print "Original data ",len(input) 
print "Compressed data ",len(final)
print "Compression ratio ",float(len(input))/len(final)




#string = ""
#a = ""
#for i in range(len(input)):
#	a += input[i]
#	if i%8 == 7 or i == len(input)-1:
#		string += chr(int(a,2))
#		a = ""
#output.write(string)

