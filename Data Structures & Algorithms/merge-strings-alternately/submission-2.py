class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        i=j=0
        res=[]
        while i<n or j<m:
            if i<n:
                res.append(word1[i])
            if j<m:
                res.append(word2[i])
            i+=1
            j+=1
        return "".join(res)
        