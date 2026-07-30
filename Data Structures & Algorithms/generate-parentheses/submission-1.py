class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(cur,opencount,closecount):
            if len(cur)==2*n:
                res.append(cur)
                return
            if opencount<n:
                backtrack(cur+"(",opencount+1,closecount)
            if closecount<opencount:
                backtrack(cur+")",opencount,closecount+1)
        backtrack("",0,0)
        return res        