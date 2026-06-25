class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for i in strs:
            op+=str(len(i))+"#"+i
        return op

    def decode(self, s: str) -> List[str]:
        op=[]
        while s:
            ind=s.find("#")
            num=int(s[:ind])
            op_string=s[ind+1:ind+num+1]
            op.append(op_string)
            s=s[ind+num+1:]
        return op

