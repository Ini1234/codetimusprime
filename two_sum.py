class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicte = []
        for i in range(len(nums)):
            checkfor= target - nums[i]
            if checkfor in dicte:
                return [i, dicte.index(checkfor)]
                
            dicte.append(nums[i])
