#include <iostream>
#include <vector>

#define NUM 31

int main(){
    std::vector<int> arr(NUM, 0);
    int std;
    for(int i = 1; i < NUM-2 ;i++){
        std::cin >> std;
        arr[std] = 1;
    }
    int one = 0;
    int two = 0;
    for(int i = 1 ; i<arr.size();i++){
        if(arr[i] == 0){
            if(one == 0) one = i;
            else two = i;
        }
    }
    int temp;
    if(one > two){
        temp = two;
        two = one;
        one = temp;
    }
    std::cout << one << '\n' << two;
    return 0;
}