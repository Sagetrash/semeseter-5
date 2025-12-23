def naiveSearch(text,pattern):
    n = len(text)
    m = len(pattern)
    i = 0
    indexList = []
    for i in range(n-m+1):
        matchLength = 0
        matchString = ''
        while matchLength < m and text[i+matchLength] == pattern[matchLength]:
            matchString = matchString + pattern[matchLength]
            matchLength+= 1
        
        if matchString == pattern:
            indexList.append([i,i+m])
            matchString = ''
    return indexList

text = "AABAACAADAABAABA"
pattern = "AABA"
match = naiveSearch(text,pattern)
print(match)