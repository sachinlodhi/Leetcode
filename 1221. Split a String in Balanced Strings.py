class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b = 0
        occ = 0
        for i in s:
            if i == 'R':
                b+=1 # rotate right
            if i == 'L':
                b-=1 # rotate left
            if b == 0:
                occ+=1 # if it has been equal left and right equal number of times.
        return occ
        

'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
 

Constraints:

1 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.
'''
