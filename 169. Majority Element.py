class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ =0
        elem = 0
        nums.sort()
        for i in set(nums):
            if occ < nums.count(i):
                occ = nums.count(i)
                if occ>len(nums)//2:
                    elem = i
                    break
        return elem
        '''Faster Approach
        nums.sort()
        if len(nums)>2:
            return nums[len(nums)//2]
        else:
            return nums[0]
        '''
    
    
    
    '''
    
    Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
'''
