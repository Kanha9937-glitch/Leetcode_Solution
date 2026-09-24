#Sl.No.:2
# Problem: Two Sum
# Difficulty: Easy
# Language: Python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]+nums[j] == target :
                    return [i, j]
        # Return an empty list if no solution is found
        return []