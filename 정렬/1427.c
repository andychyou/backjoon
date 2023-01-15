

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 10

void Swap(int *arr, int a, int b){
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}


void PrintArr(int *arr, int len){
    for(int i = 0; i < len; i++){
        printf("%d", arr[i]);
    }
}

int Partition(int *arr, int p, int r){
    int i = p-1;
    for(int j = p; j < r; j++){
        if(arr[j] > arr[r]){
            i++;
            Swap(arr, i, j);
        }
    }
    i++;
    Swap(arr, i, r);
    return i;
}

void QuickSort(int *arr, int p, int r){
    if(p<r){
        int q = Partition(arr, p, r);
        QuickSort(arr, p, q-1);
        QuickSort(arr, q+1, r);
    }
}

int IsNum(char c){
    c = c - 48;
    if(c >= 0 && c < 10){
        return 1;
    }
    else return 0;
}

int main() {

    printf("hadf");
    printf("afd");
    return 0;
}
