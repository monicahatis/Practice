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






#SOLUTION 2
'''To optimize your solution, you can reduce the time complexity from 𝑂(𝑛^3) to 𝑂(𝑛^2) by using a two-pointer approach after sorting the array. 
This eliminates the need for the triple nested loops and improves efficiency.'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to simplify the search for triplets
        nums.sort()
        result = []
        
        # Loop through each element, treating it as the first element of the triplet
        for i in range(len(nums)):
            # Skip duplicate elements to avoid duplicate triplets in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach to find the remaining two numbers
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    # If the sum is less than zero, move the left pointer to increase the sum
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to decrease the sum
                    right -= 1
        
        return result
