#include <iostream>
#include <vector>
#include <string>

int main(){
    int n;
    std::cin >> n;
    std::vector<int> arr(n,0);
    
    for(int i = 0 ; i < n; i++){
        int score = 0;
        std::string s;
        std::cin >> s;
        int temp = 0;
        for(auto it = s.begin(); it != s.end(); it++){
            if(*it == 'O'){
                temp = temp + 1;
                score += temp;
            }
            else{
                temp = 0;
            }
        }
        arr[i] = score;
    }
    for(auto &it : arr){
        std::cout << it << '\n';
    }
    return 0;
}