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
        arr[i].resize(line_n);
        for(int j = 0; j < line_n; j++){
            std::cin >> arr[i][j];
        }
    }
    for(int i = 0 ; i < n ; i++){
        double avg = 0;
        double ratio = 0;
        for(auto &it : arr[i]){
            avg += it;
        }
        avg /= (double) arr[i].size();
        for(auto &it : arr[i]){
            if(it > avg) ratio++;
        }
        ratio = ratio / (double)arr[i].size() * 100;
        ratio = std::round(ratio*1000) / 1000.0;
        std::cout << std::fixed;
        std::cout.precision(3);
        std::cout << ratio << "%\n";
    } 
    return 0;
}