from decode import *
from encode import *

def main():
    textFile = input("What is the name of the txt file you want to encode? For example \"test1.txt\ \"\n:")
    encodeAndDecode(textFile)


def encodeAndDecode(textFile):
    #ENCODE
    writeFile = "frequency.txt"
    freqTable = createFrequencyTable(textFile, writeFile)
    huffmanTree = createHuffmanTree(freqTable)
    huffmanCodes = {}
    createHuffmanCodes(huffmanTree, huffmanCodes)
    codeWriteFile = "codes.txt"
    writeHuffmanCodes(huffmanCodes, "codes.txt")
    compressedFile = "compressed.bin"
    writeCompressedFile(textFile, huffmanCodes, compressedFile)
    #DECODE
    huffman_codes = rb_codes("codes.txt")
    huffman_tree = create_huffman_tree(huffman_codes)
    
    with open("compressed.bin", "rb") as f:
        compressed_data = f.read()

    encoded_data = "".join(format(byte, '08b') for byte in compressed_data)
    decoded_text = decode_text(encoded_data, huffman_tree)

    decoded_text = decoded_text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    decoded_text = ''.join(char if char in ' ,.0123456789abcdefghijklmnopqrstuvwxyz' else ' ' for char in decoded_text)
    
 # Replace the last two characters with a period
    decoded_text = decoded_text[:-2] + "."
    with open("decoded.txt", "w") as f:
        f.write(decoded_text)

if __name__ == "__main__":
    main()