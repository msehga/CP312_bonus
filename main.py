from decode import *
from encode import *

def main():
    textFile = input("What is the name of the txt file you want to encode? \nFor example, \"test1.txt\"\n:")
    encodeAndDecode(textFile)


def encodeAndDecode(textFile):
    # Encode
    writeFile = "frequency.txt"
    freqTable = createFrequencyTable(textFile, writeFile)
    huffmanTree = createHuffmanTree(freqTable)
    huffmanCodes = {}
    createHuffmanCodes(huffmanTree, huffmanCodes)
    codeWriteFile = "codes.txt"
    writeHuffmanCodes(huffmanCodes, "codes.txt")
    compressedFile = "compressed.bin"
    writeCompressedFile(textFile, huffmanCodes, compressedFile)

    # Decode
    decodedHuffmanCodes = readCodes("codes.txt")
    decodedHuffmanTree = decodeHuffmanTree(decodedHuffmanCodes)
    with open("compressed.bin", "rb") as f:
        compressedData = f.read()
    encodedData = "".join(format(byte, '08b') for byte in compressedData)
    decodedText = decodeText(encodedData, decodedHuffmanTree)
    decodedText = decodedText.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    decodedText = ''.join(char if char in ' ,.0123456789abcdefghijklmnopqrstuvwxyz' else ' ' for char in decodedText)
    
    with open(textFile, 'r') as file:
        content = file.read()

    decodedText = decodedText[:-2] + " "

    with open("decoded.txt", "w") as f:
        f.write(decodedText)

if __name__ == "__main__":
    main()