from encode import *

# This function is used for reading the codes from codes.txt
def readCodes(filename): 
    huffmanCodes = {}
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(':')
            if parts[0]:
                char = parts[0]
            else:
                char = ' '
            code = parts[1]
            huffmanCodes[code] = char
    return huffmanCodes

# This function reconstructs the huffman tree.
def decodeHuffmanTree(huffmanCodes): 
    root = Node(None, 0)
    for code, char in huffmanCodes.items():
        node = root
        for bit in code:
            if bit == '0':
                if node.left is None:
                    node.left = Node(None, 0)
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(None, 0)
                node = node.right
        node.char = char
    return root

 # This function decodes the text.
def decodeText(encodedData, huffmanTree):
    decoded_text = ""
    current_node = huffmanTree

    for bit in encodedData:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffmanTree
            if current_node.char == ' ':
                decoded_text += ' '

    return decoded_text



