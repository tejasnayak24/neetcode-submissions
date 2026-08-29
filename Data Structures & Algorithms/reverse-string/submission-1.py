class Solution:
    def reverseString(self, s: List[str]) -> None:
        tmp=[]
        for i in range(len(s)-1,-1,-1):
            tmp.append(s[i])
        for i in range(len(s)):
            s[i]=tmp[i]
        """
        Do not return anything, modify s in-place instead.
        """
        