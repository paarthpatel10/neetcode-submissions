class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen ={}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] +=1
            else:
                seen[nums[i]] =1
        for val in seen.values():
            if val >1:
                return True
        return False


        