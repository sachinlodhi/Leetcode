class Solution:
    def firstUniqChar(self, s: str) -> int:  
        ctr = 0 # counting occurrence of characters
        for i in range(len(s)):
           ctr = s.count(s[i]) # counting number of occurrences of char i in string s
           if ctr==1:  # If it occures only ONCE
              return i
        return -1 # If the character does not occur only ONCE


'''

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

'''
