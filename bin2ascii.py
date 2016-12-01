input = open('huff_encoded.txt.txt','r').read()
output = open('ascii_encoded.txt','w+')

#import binascii

#n = int('0b' + input, 2)
#string = binascii.unhexlify('%x' % n)




string = ""
a = ""

length = len(input)%8

for i in range(len(input)-length):
	a += input[i]
	if i%8 == 7:
		string += chr(int(a.encode('utf-8').strip(),2))
		a = ""
for i in range(len(input)-length,len(input)):
	a += input[i]
string += a
string += str(length)
output.write(string)
'''
input = open('seriouslyfinal.txt','r').read()

for i in input:
	print ord(i)
'''

