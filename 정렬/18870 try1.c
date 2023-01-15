#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void Swap(int *arr, int a, int b){
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}


int Partition(int *arr, int p, int r){
    int i = p - 1;
    for(int j = p; j < r; j++){
        if(arr[j] < arr[r]){
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
        QuickSort(arr, p+1, r);
    }
}
//n^2
void PrintAnswer(int *arr1, int *arr2, int len){
    int counted = 0;
    int counted_val = 0;
    int cnt = 0;
    for(int i = 0 ; i < len; i++){
        counted_val = arr2[0];
        if(arr1[i] == counted_val){
            goto print;
        }
        else cnt++;
        for(int j = 1 ; arr2[j] < arr1[i] ;j++){
            if(counted_val != arr2[j]){
                cnt++;
                counted_val = arr2[j];
            }
        }
        print: 
            printf("%d ", cnt);
            cnt = 0;
    }
}

int main (){
    //FILE *fp = fopen("18870.txt", "r");
    FILE *fp = stdin;
    int num;
    fscanf(fp, "%d", &num);
    int *arr1 = (int*)malloc(sizeof(int)*num);
    int *arr2 = (int*)malloc(sizeof(int)*num);
    for(int i = 0; i < num; i++){
        fscanf(fp, "%d", &(arr1[i]));
        arr2[i] = arr1[i];
    }
    QuickSort(arr2, 0, num-1);
    PrintAnswer(arr1, arr2, num);
    return 0;
}