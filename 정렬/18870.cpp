#include <iostream>
#include <algorithm>
#include <vector>
int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    int n;
    std::cin >> n;
    std::vector<int> arr1(n);
    for(int i = 0 ; i < n; i++){
        std::cin >> arr1[i];
    }
    std::vector<int> arr2(arr1);
    std::sort(arr2.begin(),arr2.end());
    // std::vector<int>::iterator end;
    // end = unique(arr2.begin(), arr2.end());
    arr2.erase(unique(arr2.begin(), arr2.end()), arr2.end());
    for(int i = 0; i < n; i++){
        // auto는 자동으로 반환되는 자료형에 맞춰서 저장하는 것 같다
        auto a = std::lower_bound(arr2.begin(), arr2.end(), arr1[i]);
        std::cout << a - arr2.begin()<< ' ';
    }
    return 0;
}