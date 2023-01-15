#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef struct arr1{
    int val;
    struct arr2 *point;
}Arr1;

typedef struct arr2{
    int val;
    int counter;
    int arr1_idx;
}Arr2;

void P(Arr1 *arr1){
    for(int i = 0 ; i < 5; i++){
        printf("%p\n", (arr1[i].point));
    }
    printf("\n");
}

void PrintSort(Arr1 *arr1, Arr2 *arr2, int len){
    for(int i = 0 ; i < len; i++){
        printf("%d ", arr2[i].val);
    }
    printf("\n");
}

void Swap(Arr1 *arr1, Arr2 *arr2, int a, int b){
//    P(arr1);
  
    Arr2 temp = arr2[a];
    arr2[a] = arr2[b];
    arr2[b] = temp;
//    Arr2 *temp_point = arr1[a].point;
////    Arr2 *temp_point = &(arr2[a]);
//    arr1[a].point = arr1[b].point;
//    arr1[b].point = temp_point;
    Arr1 temp_1 = arr1[arr2[a].arr1_idx];
    arr1[arr2[a].arr1_idx] = arr1[arr2[b].arr1_idx];
    arr1[arr2[b].arr1_idx] = temp_1;
    
    
//    P(arr1);
//    PrintSort(arr1, arr2, 5);
}

int FindMedian(Arr1 *arr1, Arr2 *arr2, int a, int b, int c){
    int median;
    if(arr2[a].val >= arr2[b].val >= arr2[c].val){
        median = b;
    }
    else if(arr2[a].val >= arr2[c].val >= arr2[b].val){
        median = c;
    }
    else if(arr2[b].val >= arr2[a].val >= arr2[c].val){
        median = a;
    }
    else if(arr2[b].val >= arr2[c].val >= arr2[a].val){
        median = c;
    }
    else if(arr2[c].val >= arr2[a].val >= arr2[b].val){
        median = a;
    }
    else{
        median = b;
    }
    return  median;
}


int Partition(Arr1 *arr1, Arr2 *arr, int p, int r){
    int q = (p+r)/2;
    int median = FindMedian(arr1, arr, p, q, r);
    Swap(arr1, arr, median, r);
    int i = p - 1;
    for(int j = p; j < r; j++){
        if(arr[j].val < arr[r].val){
            i++;
            Swap(arr1, arr, i, j);
        }
    }
    i++;
    Swap(arr1, arr, i, r);
    return i;
}

void QuickSort(Arr1 *arr1, Arr2 *arr, int p, int r){
    if(p<r){
        
        int q = Partition(arr1, arr, p, r);
        
        QuickSort(arr1, arr, p, q-1);
        QuickSort(arr1, arr, q+1, r);
    }
}

void CreateAnswerVal(Arr1 *arr1, Arr2 *arr2,int len){
    if(len <= 0) return;

    int counted_val = arr2[0].val;
    arr2[0].counter = 0;

    int cnt = 0;
    for(int i = 1; i < len; i++){
        if(arr2[i].val > counted_val){
            counted_val = arr2[i].val;
            cnt++;
        }
        arr2[i].counter = cnt;

    }
}

void PrintAnswer(Arr1 *arr1, Arr2 *arr2, int len){
    for(int i = 0; i < len; i++){
        printf("%d ", arr1[i].point->counter);
    }
}



int main (){
    FILE *fp = fopen("file.txt", "r");
//    FILE *fp = stdin;
    time_t start = time(NULL);
    int num;
    fscanf(fp, "%d", &num);
    Arr1 *arr1 = (Arr1*)malloc(sizeof(Arr1)*num);
    Arr2 *arr2 = (Arr2*)malloc(sizeof(Arr2)*num);
    for(int i = 0; i < num; i++){
        fscanf(fp, "%d", &(arr1[i].val));
        arr1[i].point = &(arr2[i]);
        arr2[i].val = arr1[i].val;
        arr2[i].counter = 0;
        arr2[i].arr1_idx = i;
    }
    QuickSort(arr1, arr2, 0, num-1);
    CreateAnswerVal(arr1, arr2, num);
    PrintAnswer(arr1, arr2, num);
//    PrintSort(arr1, arr2, num);
    time_t end = time(NULL);
    printf("\n\n%lf", (double)end-start);
    return 0;
}
