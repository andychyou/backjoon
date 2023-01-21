#include <iostream>
#include <vector>

int main(){
    int a, max, idx;
    for(int i = 1; i < 10; i++){
        std::cin >> a;
        if(i == 1){
            max = a;
            idx = i;
        }
        if(max < a){
            max = a;
            idx = i;
        }
    }
    std:: cout << max << '\n' << idx;
    return 0;
}