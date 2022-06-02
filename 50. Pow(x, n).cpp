class Solution {
public:
    double myPow(double x, int n) {
//      double MAX_RES = 10000;  
//      double MIN_RES = -10000;
//      double res = 1;
//     //special cases    
//     if(x == 1)
//     {
//         return 1;
//     }
    
//     if (x == -1)
//     {
//         if(n%2==0)
//             return 1;
//         return -1;
//     }
        
        
//     if (n>0)
//     {
//     while (n){
    
//     res*=x;
//         if(res>MAX_RES)
//             return MAX_RES;
//         if(res<MIN_RES)
//             return MIN_RES;
//         if (res == 0)
//         return 0;
//     n--;
//         cout<<res<<endl;
        
//     }
    
    
// }
// else if (n<0){
//     while(n){
//     res*=(1/x);
//     n++;
//         if(res>MAX_RES)
//             return MAX_RES;
//         if(res<MIN_RES)
//             return MIN_RES;
//     if (res == 0)
//         return 0;
//     }
    
    
// }
// else{
//     res = 1;
// }
// cout<<res;
//         return res;
//     }
        return pow(x,n);
    }
};


/*
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
*/
