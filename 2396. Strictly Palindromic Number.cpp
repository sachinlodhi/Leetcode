// An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

// Given an integer n, return true if n is strictly palindromic and false otherwise.

// A string is palindromic if it reads the same forward and backward.

 

// Example 1:

// Input: n = 9
// Output: false
// Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
// In base 3: 9 = 100 (base 3), which is not palindromic.
// Therefore, 9 is not strictly palindromic so we return false.
// Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
// Example 2:

// Input: n = 4
// Output: false
// Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
// Therefore, we return false.

 

// Constraints:

// 4 <= n <= 105
// Accepted
// 37.7K
// Submissions
// 42.9K
// Acceptance Rate
// 87.7%



class Solution {
public:

bool isPalindrome(vector<int>& check)
{
    for (int i =0,  j = check.size()-1; i<=check.size()/2; ++i, --j)
    {
        if (check[i] != check [j])
        return false;
    }
    return true;
}

    
    
    vector <int> BaseConverter(int num, int base)
{
    vector <int> result;
    int t = 0;
    while(num)
    {
        result.push_back(num%base);
        num/=base;
        if(num<base)
        {
            result.push_back(num);
            break;
        }
    }
    
    // cout<<endl<<"Before Reversing : ";
    // for(int i = 0; i<result.size(); ++i)
    // {
    //     cout<<result[i]<<" ";
    // }
    // cout<<endl<<"After reversing: ";
    
     for (int i =0,  j = result.size()-1; i<result.size()/2; ++i, --j)
     {
         cout<<result[i]<<" "<<result[j]<<endl;
         t = result[i];
         result[i] = result[j];
         result[j] = t;
         
     }
     
     
    //  for(int i = 0; i<result.size(); ++i)
    // {
    //     cout<<result[i]<<" ";
    // }
    return result;
}
    
    
    bool isStrictlyPalindromic(int n) {
    
 bool flag = true;
  vector <int> response;
  for(int i = 2; i<=n-2; ++i)
  
  {
      cout<<"Checking for "<<i<<": ";
      response = BaseConverter(n,i);
      flag = isPalindrome(response);
      if (!flag){
          cout<<"Not Strictly palindrome";
        // return false;
        break;
           
      }
       
  }
    
    
    
    return flag;
    }
};
