class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=nums[0]
        max_prod=nums[0]
        cur_min=nums[0]
        for i in range(1,len(nums)):
            temp=cur_max
            cur_max=max(nums[i],cur_max*nums[i],cur_min*nums[i])
            cur_min=min(nums[i],temp*nums[i],cur_min*nums[i])
            max_prod=max(max_prod,cur_min,cur_max)
        return max_prod

                        