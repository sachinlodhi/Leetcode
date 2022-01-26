class Solution:
    def frequencySort(self, s: str) -> str:
        
        s = [i for i in s] # Converting to list
        s.sort() # Sorting 
        s = "".join(s) # Changing to string(sorted)
        # print(s)
        lou = []
        i = 0
        while i<len(s):
            cntr = s.count(s[i]) # counting number of occurence of letter
            lou.append([cntr, s[i]]) # making list of list to store as ["char", No of occurence]
            i = i + cntr
        res = []
        lou.sort(reverse=True) # revrese in decreasing order by first lement of list
        for i in lou:
            for j in range(i[0]):
                res.append(i[1]) # appending each character from sorted list as number of the occurrence of char
        return res
        
        
        
        '''
        Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
'''
