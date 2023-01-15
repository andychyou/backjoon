#include <stdio.h>
#include <stdlib.h>

void ChangeArr(int arr1[], int *arr2, int** b){
    *b = arr1;
    
    arr1[1] = 100;
    *(arr2 + 1) = 100;

}

void ChangeInt(int *n){
    *n = 100;
}

int main(){
    int* arr1 = (int*)malloc(sizeof(int)*9);
    for(int i = 0; i < 9; i++){
        arr1[i] = 9;
    }
    int* arr2 = (int*)malloc(sizeof(int)*9);
    for(int i = 0; i < 9; i++){
        arr2[i] = 9;
    }
    int n = 9;
    int *b = NULL;
    ChangeArr(arr1, arr2, &b);
    ChangeInt(n);

    return 0;
}