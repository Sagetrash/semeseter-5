class Node:
    def __init__(self,char=None,freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding: 
    def __init__(self):
        self.nodelist = []

    def createNodes(self,word):
        freqdict = {}
        for char in word:
            freqdict[char] = freqdict.get(char,0) + 1

        for char,freq in freqdict.items():
            self.nodelist.append(Node(char,freq))



    def createTree(self):
        nodes = self.nodelist
        while (len(nodes)) > 1:
            nodes = sorted(nodes,key=lambda x: x.freq)
            left = nodes.pop(0)
            right = nodes.pop(0)
            merged = Node(freq= (left.freq + right.freq))
            merged.left = left
            merged.right = right
            nodes.append(merged)
            self.nodelist = nodes
        return self.nodelist[0]

    def huffmanCode(self,node,current_code, codes):
        if node is None:
            return
        
        if node.char is not None:
            codes[node.char] = current_code
            return
        self.huffmanCode(node.left,current_code + '0',codes)
        self.huffmanCode(node.right,current_code+ '1',codes)
    
    def encode(self,word):
        self.createNodes(word)
        root = self.createTree()
        codes = {}
        self.huffmanCode(root,'',codes)
        return codes
    
        

h = HuffmanCoding()
word = "lossless"
print(h.encode(word))