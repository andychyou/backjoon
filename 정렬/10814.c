#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    int id;
    char name[101];
}Node;

void Swap(Node *arr, int a, int b){
    Node temp = arr[b];
    arr[b] = arr[a];
    arr[a] = temp;
}

void Merge(Node *arr1, Node *arr2, int low, int mid, int high){
    int curr1 = low;//low ~ mid
    int curr2 = mid+1;//mid+1 ~ high
    int k = low;
    while(curr1 <= mid && curr2 <= high){
        if(arr1[curr1].id <= arr1[curr2].id){
            arr2[k] = arr1[curr1];
            curr1++;
        }
        else if(arr1[curr1].id > arr1[curr2].id){
            arr2[k] = arr1[curr2];
            curr2++;
        }
        k++;
    }
    while(curr1 <= mid){
        arr2[k] = arr1[curr1];
        curr1++;
        k++;
    }
    while(curr2 <= high){
        arr2[k] = arr1[curr2];
        curr2++;
        k++;
    }
    //이 부분 빼먹었었음
    for(int i = low; i <= high; i++){
        arr1[i] = arr2[i];
    }
}


void MergeSort(Node *arr1, Node* arr2, int low, int high){
    if(low < high){
        int mid = (low + high) / 2;
        MergeSort(arr1, arr2, low, mid);
        MergeSort(arr1, arr2, mid+1, high);
        Merge(arr1, arr2, low, mid, high);
    }
}

void PrintArr(Node *arr, int len){
    for(int i = 0 ; i < len; i++){
        printf("%d %s\n", arr[i].id, arr[i].name);
    }
}

int main(){
    //FILE *fp = fopen("10814.txt", "r");
    FILE *fp = stdin;
    int num;
    fscanf(fp, "%d", &num);
    Node* arr1 = (Node*)malloc(sizeof(Node)*num);
    Node* arr2 = (Node*)malloc(sizeof(Node)*num);
    for(int i = 0; i < num ; i++){
        char name[101];
        fscanf(fp, "%d %s", &(arr1[i].id), name);
        //직접적으로 %s, arr[i].name을 할 수 없다고 한다
        strcpy(arr1[i].name, name);
    }
    MergeSort(arr1, arr2, 0, num-1);
    PrintArr(arr1, num);
    return 0;

}
