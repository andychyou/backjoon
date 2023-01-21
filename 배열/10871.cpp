#include <iostream>
#include <vector>


int main(){
    int n, a;
    std::cin >> n;
    std::cin >> a; 

    std::vector<int> arr(n);
    int temp;
    for(int i = 0 ; i < n ; i++){
        std::cin >> arr[i];
    }
    for(auto it : arr){
        if(it < a) std::cout << it << ' ';
    }


    return 0;
}
