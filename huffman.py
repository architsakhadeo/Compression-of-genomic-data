from heapq import heappush, heappop, heapify
from collections import defaultdict
input = open('indexed_data.txt','r').read()
input1 = open('input_file.txt','r').read()
output = open('huff_encoded.txt','w+')
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
txt = input
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq)
sim = 0
reduced = 0
symbol = []
weight = []
huffmancode = []
print "Symbol\tWeight\tHuffman Code"
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])
    symbol.append(p[0])
    weight.append(symb2freq[p[0]])
    huffmancode.append(p[1])
    reduced = reduced + symb2freq[p[0]]*len(p[1])
    #sim = sim + symb2freq[p[0]] * (8-len(str(p[1])))
#print "Sum is " + str(sim)

binary = ""
for i in txt:
	binary += huffmancode[symbol.index(i)]
output.write(binary)

print symbol
print weight
print huffmancode

print "Weight is " + str(len(txt))
print "Reduced is " + str(int(reduced/8))
print "Compression ratio is " + str(float(len(txt))/int(reduced/8))
print "Cummulative compression ratio is " + str(float(len(input1))/int(reduced/8))
