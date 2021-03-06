# Faster and Shorter Code

def findTheDifference(self, s: str, t: str) -> str:
            s = "".join(sorted(s))
            t = "".join(sorted(t))
            for i in range(len(s)):
                if s[i]!=t[i]:
                    return t[i]
            return t[len(t)-1]
            
            
            
# Slower and Longer Code

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = [i for i in s]
        t = [i for i in t]
        s.sort()
        t.sort()
        s = "".join(s)
        t = "".join(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]
        return t[len(t)-1]
      
      
'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
'''
