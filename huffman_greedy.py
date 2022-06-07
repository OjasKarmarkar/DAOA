codes = dict()

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # freqability of symbol
        self.freq = freq

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

def calc_node(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        calc_node(node.left, newVal)
    if(node.right):
        calc_node(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes

data = input("Enter String to Compresss : ")

freq = {}

for ch in data:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

freq = sorted(freq.items(), key=lambda x: x[1])
nodes = []

for item in freq:
    nodes.append(Node(item[1], item[0]))

while(len(nodes) > 1):
    nodes = sorted(nodes, key=lambda x: x.freq)
    right = nodes[0]
    left = nodes[1]
    
    left.code = 0
    right.code = 1
    
        # combine the 2 smallest nodes to create new node
    newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
    
huffman_encoding = calc_node(nodes[0])
print("symbols with codes", huffman_encoding)