class Solution:
    """
    Maintain a subset of elements (the "window") that slides through a data structure, such as an array or string.
    The window can be fixed-size or variable-size, expanding or contracting based on problem-specific conditions.
    Use two pointers to define the window's boundaries, adjusting them as needed to meet the problem's criteria.
    Continuously update results (e.g., maximum sum, minimum length) as the window slides.

    If there's a preset subarray, we add/subtract from the beginning and end
    If there isn't, we use pointers at the beginning
    """
    def findMaxAverage(self, nums:list, k):
        current_sum = max_sum = float(sum(nums[:k]))

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum / k
    
    def maxVowels(self, s: str, k: int):
        vowels = "aeiou"
        current_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        for j in range(k, len(s)):
            if s[j-k] in vowels:
                current_vowels -= 1
            if s[j] in vowels:
                current_vowels += 1
                if current_vowels > max_vowels:
                    max_vowels = current_vowels
        return max_vowels
    
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = max_count = zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            current_count = right - left + 1
            max_count = max(max_count, current_count)
        return max_count
    
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        max_count = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_count = right - left #We always delete 1 so we don't +1
            max_count = max(max_count, current_count)
        return max_count
        
solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
print(solution.findMaxAverage([5], 1))
print(solution.findMaxAverage([3,3,4,3,0], 3))
print(solution.findMaxAverage([0,1,1,3,3], 4))
print(solution.findMaxAverage([-1], 1))
print(solution.findMaxAverage([0,4,0,3,2], 1))
print(solution.maxVowels("abciiidef", 3))
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(solution.longestSubarray([1,1,0,1]))
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(solution.longestSubarray([1,1,1]))