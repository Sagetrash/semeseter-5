class Node:
    def __init__(self,char=None,freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding: 
    def __init__(self,word):
        self.word = word
        self.nodelist = []
        self.encode()

    def createNodes(self,word):
        freqdict = {}
        for char in word:
            freqdict[char] = freqdict.get(char,0) + 1

        for char,freq in freqdict.items():
            self.nodelist.append(Node(char,freq))



    def createTree(self):
        while (len(self.nodelist)) > 1:
            self.nodelist = sorted(self.nodelist,key=lambda x: x.freq)
            left = self.nodelist.pop(0)
            right = self.nodelist.pop(0)

            merged = Node(freq= (left.freq + right.freq))
            merged.left = left
            merged.right = right
            
            self.nodelist.append(merged)
        return self.nodelist[0]

    def huffmanCode(self,node,current_code, codes):
        if node is None:
            return
        
        if node.char is not None:
            codes[node.char] = current_code
            return
        self.huffmanCode(node.left,current_code + '0',codes)
        self.huffmanCode(node.right,current_code+ '1',codes)
    
    def encode(self):
        self.createNodes(self.word)
        root = self.createTree()
        codes = {}
        self.huffmanCode(root,'',codes)
        self.codes = codes
    
    def getCodes(self): return self.codes
    def codeWord(self): return ''.join(self.codes[char] for char in self.word)

word = input("Enter the word you want to encode:")
h = HuffmanCoding(word)
print(h.getCodes())
print(h.codeWord())