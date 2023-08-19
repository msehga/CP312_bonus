from encode import *

def readCodes(filename): # This function is used for reading the codes from codes.txt
    huffman_codes = {}
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(':')
            char = parts[0] if parts[0] else ' ' # If the character part is empty, then it represents space
            code = parts[1]
            huffman_codes[code] = char
    return huffman_codes


def create_huffman_tree(huffman_codes): #this function reconstructs the huffman tree.
    root = Node(None, 0)
    for code, char in huffman_codes.items():
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

def decode_text(encoded_data, huffman_tree): #this function decodes the text.
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree
            if current_node.char == ' ':
                decoded_text += ' '

    return decoded_text

def main(): #main function is used to run the program
    huffman_codes = readCodes("codes.txt")
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


