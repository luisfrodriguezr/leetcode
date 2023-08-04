class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)return false;
        // Create a copy of the number
        int x_copy = x;
        long new_x = 0;
        while(x_copy){
            new_x*=10; new_x+=x_copy%10;
            x_copy/=10;
        }
        return x==new_x?true:false;
    }
};