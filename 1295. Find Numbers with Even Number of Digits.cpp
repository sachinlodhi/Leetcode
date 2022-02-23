class Solution {
public:
    int findNumbers(vector<int>& nums) {
        
    
    ostringstream str1; // buffer to save individual numbers into this variable
    string t;
    int len = 0;
    int even = 0; //coutning number of digits having even length
    for (int i = 0; i<nums.size(); ++i)
    {   
        
        str1<<nums[i]; //pushing number into str1 variable
        t = str1.str(); //Coversion into string and assignment into t variable
        if((t.length() - len)%2 ==0){ // check if the current number length i.e. current lenght - old lenght is even or not
            even++;
        }
        len = t.length();// storing current lenght
        
    }
 return even;

    
    
    }
};


/*


Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105

/*


