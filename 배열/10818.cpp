#include <iostream>
#include <vector>

int main(){
    int n, temp;
    std::cin >> n;
    int max, min;
    for(int i = 0; i < n; i++){
        std::cin >> temp;
        if(i == 0) max = min = temp; 
        if(max < temp) max = temp;
        if(min > temp) min = temp;
    }
    std::cout << min << ' ' << max;
    return 0;
}