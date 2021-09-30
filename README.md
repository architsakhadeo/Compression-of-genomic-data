`input_file.txt` is the input genome file on which we apply compression.

## High-level instructions for the processing stages

**COMPRESSION STARTS**

	`python freq_index.py`

	`python huffman.py`

	`python bin2ascii.py`
			
**COMPRESSION ENDS**

**DECOMPRESSION STARTS**

	`python ascii2bin.py`

	`python dehuffman.py`

	`python defreq_deindex.py`

**DECOMPRESSION ENDS**

--------------------------------------------------------------------------------

## Detailed instructions for the processing stages

**COMPRESSION STARTS**

1) `python freq_index.py`

takes input as `input_file.txt` = DNA data

gives output as `Jude.txt` = without '\n' key,  `dict.txt` = dictionary of patterns, `frequency.txt` = frequency model,  `pattern_list.txt` = list of patterns, `index_list.txt` = list of indices, `indexed_data.txt` = indexed data	

--------------------------------------------------------------------------------
2) `python huffman.py`

takes input as `indexed_data.txt` = indexed data for huffman encoding, `input_file.txt` = DNA data for calculating compression ratio

gives output as `huff_encoded.txt` = huffman encoded data	

--------------------------------------------------------------------------------

3) `python bin2ascii.py`

takes input as `huff_encoded.txt` = huffman encoded data

gives output as `ascii_encoded.txt` = huffman encoded to ascii unicode chars

--------------------------------------------------------------------------------
		
**COMPRESSION ENDS**

*DECOMPRESSION STARTS*
1) `python ascii2bin.py`

takes input as `ascii_encoded.txt` = huffman encoded to ascii unicode chars

gives output as `ascii_decoded.txt` = ascii unicode to binary

--------------------------------------------------------------------------------

2) `python dehuffman.py`

takes input as `ascii_decoded.txt` = binary huffman encoded file

gives output as `huff_decoded.txt` = huffman to indexed file
		
--------------------------------------------------------------------------------

3) `python defreq_deindex.py`

takes input as `pattern_list.txt` = list of patterns, `index_list.txt` = list of indices, `huff_decoded.txt` = indexed file

gives output as `decompressed.txt` = indexed to frequency to DNA data

**DECOMPRESSION ENDS**

