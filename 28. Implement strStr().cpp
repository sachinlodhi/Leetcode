class Solution {
public:
    int strStr(string haystack, string needle) {
        
    
    if (size(needle) == 0){
        return 0;
    }
    
    int pos = haystack.find(needle);
    return pos;
 
    return -1;
    }
};
