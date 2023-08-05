class Solution {
public:
    int reverse(int x) {
        int response = 0;
        while(x){
            response*=10; response+=x%10;
            x/=10;
            if(response!=0){
                if(x>0 && INT_MAX/response<10)return 0;
                if(x<0 && (INT_MIN+1)/response<10)return 0;
            }
        }
        return response;
    }
};