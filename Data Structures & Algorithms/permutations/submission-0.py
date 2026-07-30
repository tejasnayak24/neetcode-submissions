class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def dfs():
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                dfs()
                path.pop()
        dfs()
        return res
        