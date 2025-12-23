def createLPS(pattern):
    n = len(pattern)
    lps = [0]*n
    i = 1
    length = lps[i-1]
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length -1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMPmatch(text,pattern):
    lps = createLPS(pattern)
    n = len(text); m = len(pattern)
    i,j = 0,0
    resultList = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                resultList.append([i-m,i-1])
                j = lps[j-1]
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return resultList

txt = "aabaacaadaabaaba"
pattern = "aaba"
res = KMPmatch(txt,pattern)
print(res)