class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        s = 0
        e = len(nums) - 1
        while True:
            if target>nums[mid]:
                s = mid + 1 # target is in second half
            elif target<nums[mid]:
                e = mid - 1 # target is in first half
            elif target == nums[mid]:
                return mid # found
            mid = (s + e) // 2
            if s>mid:
                return mid+1

            mid = (s + e) // 2
            
            
'''

        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
