import os

import LZW as lzw

whatMethod = input('method; single character LZW-l: ')
whatToDo = input('compress or decompress- c/d: ')


#change directories to compress/decompress
filename = 'input/inputToCompress.txt'
with open(filename, 'r') as file:
    dataToC = file.read()
    
filename = 'input/inputToDecompress.txt'
with open(filename, 'r') as file:
    dataToDc = file.read()

if whatToDo == 'c': #compressing
    if whatMethod == 'l':
        compressed_data = lzw.compress(dataToC)
        compressed_str = " ".join(map(str, compressed_data))
        print(f'Compressed data:  {compressed_str}') #prints numbers in this form 250 100 235... instead of [250, 100, 235,...]
    
        #compare size
        with open('output/compressed.txt', 'w') as tester:
            tester.write(compressed_str)

        original_size = os.path.getsize('input/inputToCompress.txt')
        compressed_size = os.path.getsize('output/compressed.txt')
        print(f'Original size: {original_size} bytes')
        print(f'Compressed size: {compressed_size} bytes')


    elif whatMethod == 'aaa':
        pass
    
else: #decompressing   
    dataToDc = list(map(int, dataToDc.split())) #list of ints from string
    
    if whatMethod == 'l':
        decompressed_data = lzw.decompress(dataToDc)
        print(f'Decompressed data: {decompressed_data}')

  
    elif whatMethod == 'aaa':
        pass
