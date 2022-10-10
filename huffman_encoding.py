#Class for Huffman Node
class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huff = '' 

#Helper function to calc the prob of the characters in the text file
def calculate_char (data):
    chars = dict()
    for element in data:
        if chars.get(element) == None:
            chars[element] = 1
        else:
            chars[element] += 1
    return chars

codes = dict()
def calc_size(node, bit=''):
    prefixCode = bit + str(node.huff)
    if(node.left):
        calc_size(node.left, prefixCode)
    if(node.right):
        calc_size(node.right, prefixCode)
    if(not node.left and not node.right):
        codes[node.char] = prefixCode
    return codes

#Function for finding the difference in bits before and after encoding
def Total_diff(contents,encoding):
    before_compression = 8 * len(contents) #1 character = 8 bits
    after_compression = 0
    chars = encoding.keys()
    for char in chars:
        count = contents.count(char)
        after_compression += count * len(encoding[char]) # bits after encoding
    print("Size of file before using huffman: ", before_compression)
    print("Size of file after using huffman: ", after_compression)


def getFile(filename):
    with open(filename) as f:
        x = f.read()
    return x


def huffman_encoding(contents):
    char_calc = calculate_char(contents)
    chars = char_calc.keys()
    frequncey = char_calc.values()

    nodes = []
   

    for char in chars:
        nodes.append(Node(char_calc.get(char), char))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        left.huff = 0
        right = nodes[1]
        right.huff = 1

        parentNode = Node(left.freq+right.freq, left.char+right.char, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(parentNode)

    
    print("Table of prefix codes: ")
    encoding = calc_size(nodes[0])
    print(encoding)
    

    Total_diff(contents, encoding)


print("Enter file name (.txt)")
fileN=input()
x=getFile(fileN)
huffman_encoding(x)
