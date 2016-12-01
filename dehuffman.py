symbol = ['3', 'a', '4', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '5', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '6', '0', '1', '7', '8', '2', '9']

huffmancode = ['01', '101', '1001', '0010', '10000', '00110', '00011', '00010', '00001', '00000', '111110', '111111', '111101', '111100', '111011', '111001', '111010', '111000', '110111', '110110', '110101', '110001', '110010', '110011', '110100', '110000', '100011', '001111', '100010', '0011101', '001110010', '001110011', '001110001', '0011100001', '00111000000', '00111000001']


input = open('ascii_decoded.txt','r').read()
string = ""
output = open('huff_decoded.txt','w+')
j = 0

while j <= len(input) - 1:
	#print j
	k = j
	string = ""
	for i in range(len(huffmancode)):
		if huffmancode[i] != input[j:j+len(huffmancode[i])]:
			#print huffmancode[i], input[j:j+len(huffmancode[i])-1]
			continue
		else:
			#print "Hey"
			string += symbol[i]
			output.write(string)
			j = j + len(huffmancode[i])
			break
	if k == j:
		break		

