#include <iostream>
#include <vector>
#include <cmath>

int main(){
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> arr(n);
    for(int i = 0 ; i < n ; i++){
        int line_n;
        std::cin >> line_n;
        std::vector<int> arr_r(line_n);
        for(int j = 0; j < line_n; j++){
            std::cin >> arr_r[j];
        }
        //2d vector의 row가 arr_r를 가리키도록 할 수 있을까
        arr[i] = arr_r;
    }
    for(int i = 0 ; i < n ; i++){
        double avg = 0;
        for(auto &it : arr[i]){
            avg += it;
        }
        avg /= (double) arr[i].size();
        avg = std::round(avg*1000) / 1000.0;
        std::cout << avg;
    } 
    return 0;
}