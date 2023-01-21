#include <iostream>
#include <vector>


int main(){
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for(int i = 0 ; i < n; i++){
        std::cin >> arr[i];
    }
    int v;
    std::cin >> v;
    int cnt = 0;
    for(auto it = arr.begin() ; it != arr.end(); it++){
        if(*it == v) cnt++;
    }
    std:: cout << cnt;

    return 0;
}