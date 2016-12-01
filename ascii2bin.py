input = open('ascii_encoded.txt','r').read()
output = open('ascii_decoded.txt','w+')
string = ""
for i in range(len(input)-int(input[-1])-1):
	a = bin(ord(input[i]))
	a = a[2:]
	for j in range(8-len(a)):
		a = '0' + a
	string += a
for j in range(i+1,len(input)-1):
	string += input[j]
output.write(string)
#print len(input)
