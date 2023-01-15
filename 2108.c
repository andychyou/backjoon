#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ARR_LEN 8001


int Mean(int sum, int len){
    //분자가 double이어야 소수점 나옴 분자가 int면 나머지 없이 계산됨
    double mean = sum / (double)len;
    return round(mean);
}


int Median(int arr[], int len){
    int cnt = 0;
    int found = 0;
    int i = ARR_LEN-1;
    int median;
    while(found == 0){
        if(arr[i] != 0){
            cnt += arr[i];
            if(cnt >= len/2+1){
                found = 1;
                median = i - 4000;
            }
        }
        i--;
    }
    return  median;
}

int MostFrequent(int arr[]){
    int most_freq;
    int freq_cnt = -1;
    int second_smallest = 0;
    for(int i = 0 ; i < ARR_LEN; i++){
        if(arr[i] > freq_cnt){
            most_freq = i - ARR_LEN/2;
            freq_cnt = arr[i];
            second_smallest = 0;
        }
        else if(arr[i] == freq_cnt && second_smallest == 0){
            most_freq = i - ARR_LEN/2;
            second_smallest = 1;
        }
    }
    return most_freq;
}

int Range(int arr[]){
    int l = 0;
    int r = ARR_LEN - 1;
    int range;
    for(int i = 0; i < ARR_LEN; i++){
        if(arr[i]) {
            l = i - ARR_LEN/2;
            break;
        }
    }
    for(int i = ARR_LEN-1; i >= 0; i--){
        if(arr[i]) {
            r = i - ARR_LEN/2;
            break;
        }
    }
    range = r - l;
    return range;
}

int main(){
    //FILE *fp = fopen("2108.txt", "r");
    FILE *fp = stdin;
    int N;
    fscanf(fp, "%d", &N);
    int arr[ARR_LEN] = {0,};
    int sum = 0;
    int v;
    for(int i = 0 ; i < N; i++){
        fscanf(fp, "%d", &v);
        arr[v+ARR_LEN/2]++;
        sum += v;
    }
    int mean = Mean(sum, N);
    int median = Median(arr, N);
    int most_freq = MostFrequent(arr);
    int range = Range(arr);
    printf("%d\n%d\n%d\n%d\n", mean, median, most_freq, range);
    return 0;
}