#include <iostream>
#include <vector>

#define DIV_NUM 42


int main(){
    int a;
    std::vector<int> arr(DIV_NUM, 0);
    for(int i = 0; i < 10; i++){
        std::cin >> a;
        arr[a % DIV_NUM]++;
    }
    int cnt = 0;
    for(auto &i : arr){
        if(i != 0) cnt++;
    }
    std::cout << cnt;
    return 0;
}