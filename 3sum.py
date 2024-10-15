#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

#SOLUTION 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sums = {}
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_answer = sorted([nums[i], nums[j], nums[k]])
                        three_sums[str(sorted_answer)] = [nums[i], nums[j], nums[k]]
        return three_sums.values()


'''The code uses three nested loops to generate all possible triplets from the array:
The outermost loop (i): Goes from the first element to the second last.
The middle loop (j): Starts from i+1, ensuring j is always after i.
The innermost loop (k): Starts from j+1, ensuring k is always after j.
This ensures that you don't pick the same index twice and always get distinct triplets.

The triplet [nums[i], nums[j], nums[k]] is sorted using sorted([nums[i], nums[j], nums[k]]). 
Sorting ensures that triplets like [1, -1, 0] and [0, 1, -1] are treated as the same triplet.

The sorted triplet is converted into a string str(sorted_answer) and used as the key in the three_sums dictionary. 
This ensures that if the same triplet appears again, it will overwrite the previous one, effectively preventing duplicates.'''

#The triple nested loops make this approach very slow, especially for large input sizes, as it has a time complexity of 𝑂(𝑛^3), 
# where 𝑛 is the number of elements in the array.