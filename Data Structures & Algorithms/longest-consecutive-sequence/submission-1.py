class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        res = 0
        count = 1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i -1] +1:
                count +=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = max(res,count)
                count =1
        return max(res,count)
