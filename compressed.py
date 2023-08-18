# Create a Node class for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def createFrequencyTable(textPath, writePath):
    # ... same as before ...
     #CREATE DICT TO STORE COUNT OF CHARS
    alpha = " ,.0123456789abcdefghijklmnopqrstuvwxyz"
    alphaDict = {}
    for char in alpha:
        alphaDict[char] = 0
    #READ FILE AND UPDATE COUNT OF CHARS
    readFile = open(textPath, "r")
    while True:
        char = readFile.read(1)
        if not char:
            break
        if char.isspace():
            alphaDict[" "] += 1
        elif char.lower() in alphaDict:
            alphaDict[char.lower()] += 1
    readFile.close()
    #WRITE CHAR COUNTS TO NEW FILE
    writeFile = open(writePath, "w+")
    totalEntries = len(alphaDict)
    for index, (key, val) in enumerate(alphaDict.items()):
        writeFile.write(key + ":" + str(val))
        if index < totalEntries - 1:
            writeFile.write("\n")
    writeFile.close()
    #SORT DICTIONARY AND RETURN
    sortedDict = dict(sorted(alphaDict.items(), key=lambda item: item[1]))
    return sortedDict


def createHuffmanTree(freqTable):
    queue = [Node(char, freq) for char, freq in freqTable.items()]
    queue.sort(reverse=True)  # Sort in descending order so that we can pop from the end

    while len(queue) > 1:
        # Pop two nodes with smallest frequencies
        right = queue.pop()
        left = queue.pop()

        # Create a new node with these two nodes as children
        newNode = Node(None, left.freq + right.freq)
        newNode.left = left
        newNode.right = right

        # Add the new node back to the queue and re-sort
        queue.append(newNode)
        queue.sort(reverse=True)

    return queue[0]  # Return the root of the Huffman Tree


def createHuffmanCodes(root, codeDict, currentCode=''):
    if root is None:
        return

    if root.char is not None:  # Leaf node
        codeDict[root.char] = currentCode
        return

    createHuffmanCodes(root.left, codeDict, currentCode + '0')
    createHuffmanCodes(root.right, codeDict, currentCode + '1')
def writeHuffmanCodes(codeDict,writePath):
    writeFile = open(writePath, "w+")
    total_entries = len(codeDict)
    for index, (key, val) in enumerate(codeDict.items()):
        writeFile.write(key + ":" + str(val))
        if index < total_entries - 1:
            writeFile.write("\n")
    writeFile.close()
    return


# def writeCompressedFile(textPath, huffmanCodes, compressedPath):
#     with open(textPath, 'r') as textFile:
#         with open(compressedPath, 'wb') as compressedFile:
#             byteBuffer = ''
#             while True:
#                 char = textFile.read(1)
#                 if not char:
#                     break
#                 # Look up the Huffman code for this character
#                 if char.isspace():
#                     charCode = huffmanCodes[' ']
#                 else:
#                     charCode = huffmanCodes.get(char.lower(), '')
#                 byteBuffer += charCode
#                 # Write out in chunks of 8 bits
#                 while len(byteBuffer) >= 8:
#                     byte = byteBuffer[:8]
#                     byteBuffer = byteBuffer[8:]
#                     # Convert the 8-bit string to an integer, and write as a single byte
#                     compressedFile.write(bytes([int(byte, 2)]))
#                     print(byte + ":" + charCode + ":" + char)
#             # Write any remaining bits, padding with zeros if necessary
#             if byteBuffer:
#                 byteBuffer = byteBuffer.ljust(8, '0')
#                 compressedFile.write(bytes([int(byteBuffer, 2)]))

def writeCompressedFile(textPath, huffmanCodes, compressedPath):
    bits = []
    with open(textPath, 'r') as textFile:
        while True:
            char = textFile.read(1)
            if not char:
                break
            if char.isspace():
                charCode = huffmanCodes[' ']
            else:
                charCode = huffmanCodes.get(char.lower(), '')
            # Add the Huffman code to the bit list
            bits.extend([int(bit) for bit in charCode])

    # Convert the bit list to a byte array
    byteArray = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        # Convert the byte list to an integer and add to the byte array
        byteArray.append(int(''.join(map(str, byte)), 2))
        print(byte)
        print(char + charCode)
        

    # Write the byte array to the compressed file
    with open(compressedPath, 'wb') as compressedFile:
        compressedFile.write(byteArray)

    #charCode should be the binary representation of the character we scanned in the text
    #bits is the array where each element in the array represents a bit in charCode
    #
    

        





textFile = "test1.txt"
writeFile = "frequency.txt"
freqTable = createFrequencyTable(textFile, writeFile)
huffmanTree = createHuffmanTree(freqTable)
huffmanCodes = {}
createHuffmanCodes(huffmanTree, huffmanCodes)
codeWriteFile = "codes.txt"
writeHuffmanCodes(huffmanCodes, "codes.txt")

binNum = 0
aValue = huffmanCodes['a']
#'a' = '1001'
for bit in aValue:
    binNum = binNum * 2 + int(bit)
print(binNum)
import sys
print(sys.getsizeof(binNum))

compressedFile = "compressed.bin"
writeCompressedFile(textFile, huffmanCodes, compressedFile)
#binNum is now 9
#'1001' = 1009 (binary) = 9 (decimal)
#nevermind, 9 is no longer stored as 1001, it is 
#stored as 0000 0000 0000 0000 0000 0000 1001.





