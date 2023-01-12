/*
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

 

Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
 

Constraints:

1000 <= num <= 9999
Accepted
69.4K
Submissions
79.2K
Acceptance Rate
87.6%
*/

class Solution {
public:
    int minimumSum(int num) {
    int ar[4];
    num*=10;
    int t = -1;
    // Extracting each digit
    while(num/=10)
    {
        ar[++t] = num%10;
        // num/=10;
    }
   
    //Bubble sort to extract two smallest number in the beginning
    for(int i = 0; i<4;++i)
      for(int j = 0; j<4;++j)
           if (ar[i]<ar[j])
            {
                t = ar[j];
                ar[j] = ar[i];
                ar[i] = t;
            }
      
    // Making combo and returning result(summation of generated comobos)
    return (ar[0] * 10 + ar[2])+(ar[1] * 10 + ar[3]);
   
    }
    
   
   

    
   
};
