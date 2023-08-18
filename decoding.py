class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def read_codes(filename):
    huffman_codes = {}
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            char, code = line.strip().split(':')
            huffman_codes[code] = char
    return huffman_codes

def build_huffman_tree(huffman_codes):
    root = HuffmanNode(None, 0)
    for code, char in huffman_codes.items():
        node = root
        for bit in code:
            if bit == '0':
                if node.left is None:
                    node.left = HuffmanNode(None, 0)
                node = node.left
            else:
                if node.right is None:
                    node.right = HuffmanNode(None, 0)
                node = node.right
        node.char = char
    return root

def decode_text(encoded_data, huffman_tree):
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

    return decoded_text

def main():
    huffman_codes = read_codes("codes.txt")
    huffman_tree = build_huffman_tree(huffman_codes)
    
    with open("compressed.bin", "rb") as f:
        compressed_data = f.read()

    encoded_data = "".join(format(byte, '08b') for byte in compressed_data)
    decoded_text = decode_text(encoded_data, huffman_tree)

    decoded_text = decoded_text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    decoded_text = ''.join(char.lower() if char.isalpha() else char for char in decoded_text if char in ' ,.0123456789abcdefghijklmnopqrstuvwxyz')

    with open("decoded.txt", "w") as f:
        f.write(decoded_text)

if __name__ == "__main__":
    main()
