class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
            
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return (ispalindrome(l,r-1) or ispalindrome(l+1,r))
            l+=1
            r-=1
        return True



        