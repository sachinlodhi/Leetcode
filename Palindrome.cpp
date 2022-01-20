class Solution {
public:
    bool isPalindrome(int x) {
        
        long int is_P = x, t=0;
        if (x>=0){
        while(x){
            t*=10;
            t += x%10;
            x/=10;
        }
        
        if (is_P == t){
            return true;
        }}
        
        return false;
    }
};
