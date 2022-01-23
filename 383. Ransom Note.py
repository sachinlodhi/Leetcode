class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst1 = []
        lst1[:0] = ransomNote
        lst2 = []
        lst2[:0] = magazine
        
        for i in lst1:
            if i in lst2:
                lst2.remove(i)
                print("yes")
            else:
                return False
        if len(lst1)>0:
            return True
        return False
        
        
        
        
        '''
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
