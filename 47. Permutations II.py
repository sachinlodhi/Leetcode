class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = []
        perm = permutations(nums)
        for i in list(perm):
            if list(i) not in l:
                 l.append(list(i))
                
        return l
      
      
'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
