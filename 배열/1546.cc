#include <iostream>
#include <vector>
#include <algorithm>
int main(){
    int n;
    std::cin >> n;
    std::vector<double> arr(n,0);
    for(int i = 0 ;i<n;i++){
        std::cin >> arr[i];
    }
    double largest = (double)*max_element(arr.begin(), arr.end());
    for(auto it = arr.begin(); it < arr.end(); it++){
        *it = *it/largest*100;
    }
    double avg = 0;
    for(auto it = arr.begin(); it < arr.end(); it++){
        avg += *it;
    }
    std::cout.precision(20);
    std::cout << avg/n;
    return 0;
}