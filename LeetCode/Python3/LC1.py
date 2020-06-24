"""
LeetCode - Problem 1
Allan Hieng
"""


def twoSum (nums, target):
    diffDict = {} #will hold the desired difference : index pair

    for i in range (len(nums)):
        if nums[i] in diffDict: 
            return [diffDict.get(nums[i]), i]
        else:
            diff = target - nums[i]
            diffDict[diff] = i