# Create a Node class for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # This is needed for sorting. Without this it won't be easy to compare Huffman tree nodes 
    def __lt__(self, other):
        return self.freq < other.freq

def createFrequencyTable(textPath, writePath):
    # Create dict to store count of chare
    alpha = " ,.0123456789abcdefghijklmnopqrstuvwxyz"
    alphaDict = {}
    for char in alpha:
        alphaDict[char] = 0

    # Read file and update count of chars
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

    # Write char into the file
    writeFile = open(writePath, "w+")
    totalEntries = len(alphaDict)
    for index, (key, val) in enumerate(alphaDict.items()):
        writeFile.write(key + ":" + str(val))
        if index < totalEntries - 1:
            writeFile.write("\n")
    writeFile.close()

    #Sort dictionary and return 
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

    if root.char is not None:  
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
        
    # Write the byte array to the compressed file
    with open(compressedPath, 'wb') as compressedFile:
        compressedFile.write(byteArray)

