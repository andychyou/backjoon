#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>




int Partition(int* arr, int p, int r){
    int i = p - 1;
    for(int j = p; j <= r-1; j++){
        if(arr[r] > arr[j]){
            i++;
            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }
    i++;
    int temp = arr[r];
    arr[r] = arr[i];
    arr[i] = temp;
    return i;
}

void QuickSort(int arr[], int p, int r){
    if(p < r){
        int q = Partition(arr, p, r);
        QuickSort(arr, p, q-1);
        QuickSort(arr, q+1, r);
    }
}


int main(){
    //FILE *fp = fopen("2750.txt", "r");  
	FILE *fp = stdin;
    int num, i;
    fscanf(fp, "%d", &num);
    int* arr = (int*)malloc(sizeof(int)*num);
    for(int x = 0 ; x < num; x++){
        fscanf(fp, "%d", &i);
        arr[x] = i;
    }
    QuickSort(arr, 0, num-1);
    for(int i = 0; i < num; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}