#include <stdio.h>
#include <stdlib.h>


void Swap(int arr[], int a, int b){
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}


int FindMedianIndex(int arr[], int one, int two, int three){
    int median_idx;
    if(arr[one] >= arr[two] && arr[two]>= arr[three]){
        median_idx = two;        
    }
    else if(arr[one] >= arr[three] && arr[three] >= arr[two]){
        median_idx = three;
    }
    else if(arr[two] >= arr[one] && arr[one] >= arr[three]){
        median_idx = one;
    }
    else if(arr[two] >= arr[three] && arr[three] >= arr[one]){
        median_idx = three;
    }
    else if(arr[three] >= arr[one] && arr[one] >= arr[two]){
        median_idx = one;
    }
    else if(arr[three] >= arr[two] && arr[two] >= arr[one]){
        median_idx = two;
    }
    return median_idx;
}

int M3_Partition(int arr[], int p, int r){
    int one = p;
    int two = (p+r)/2;
    int three = r; 
    int median_idx = FindMedianIndex(arr, one, two, three);
    Swap(arr, median_idx, r);

    //i는 피벗보다 작은 수가 포함되는 경계(마지막에 return할 때는 i번째 index는 피벗임)
    //j는 현재 비교하는 수의 idx
    int i = p - 1;
    for(int j = p; j <= r-1; j++){
        if(arr[r] > arr[j]){
            i++;
            Swap(arr, i, j);
        }
    }
    //피벗과 i의 위치 바꾸기
    i++;
    Swap(arr, i, r);
    //피벗의 위치 반환
    return i;
}



// void QuickSort(int arr[], int p, int r){
//     if(p<r){
//         int q = M3_Partition(arr, p, r);
//         QuickSort(arr, p, q-1);
//         QuickSort(arr, q+1, r);
//     }
// }



void PrintArr(int arr[], int len){
    for(int i = 0 ; i < len ; i++){
        printf("%d\n", arr[i]);
    }
}
void heapify(int arr[], int cnt, int here)
{
    int largest = here;
    int l = 2 * here + 1;
    int r = 2 * here + 2;
    if (l < cnt && arr[l] > arr[largest])
        largest = l;
    if (r < cnt && arr[r] > arr[largest])
        largest = r;
    if (largest != here) {
        int temp = arr[here];
        arr[here] = arr[largest];
        arr[largest] = temp;
        heapify(arr, cnt, largest);
    }

}

void createHeap(int heap[], int cnt){ 
    for(int check = cnt / 2 - 1; check >=0 ; check--){
        heapify(heap, cnt, check);
    }
}


void heapSort(int arr[], int cnt)
{
    createHeap(arr, cnt);
    int last = cnt - 1;
    while(last > 0 ){
        int temp = arr[0];
        arr[0] = arr[last];
        arr[last] = temp;
        heapify(arr, last--, 0);
    }
}


int main(){
    //FILE *fp = fopen("2751.txt", "r");
    FILE *fp = stdin;
    int N;
    fscanf(fp, "%d", &N);
    int* arr = (int*)malloc(sizeof(int)*N);
    for(int i = 0; i < N ; i++){
        fscanf(fp, "%d", &arr[i]);
    }
    // QuickSort(arr, 0, N-1);
    heapSort(arr, N);
    PrintArr(arr, N);
    return 0;
}