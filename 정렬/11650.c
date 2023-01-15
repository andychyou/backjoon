#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int x,y;
}Node;

int FindMedianIndex(Node arr[], int one, int two, int three){
    int median_idx;
    if(arr[one].x >= arr[two].x && arr[two].x>= arr[three].x){
        median_idx = two;        
    }
    else if(arr[one].x >= arr[three].x && arr[three].x >= arr[two].x){
        median_idx = three;
    }
    else if(arr[two].x >= arr[one].x && arr[one].x >= arr[three].x){
        median_idx = one;
    }
    else if(arr[two].x >= arr[three].x && arr[three].x >= arr[one].x){
        median_idx = three;
    }
    else if(arr[three].x >= arr[one].x && arr[one].x >= arr[two].x){
        median_idx = one;
    }
    else if(arr[three].x >= arr[two].x && arr[two].x >= arr[one].x){
        median_idx = two;
    }
    return median_idx;
}

void Swap(Node *arr, int a, int b){
    int x,y;
    x = arr[a].x;
    y = arr[a].y;
    arr[a].x = arr[b].x;
    arr[a].y = arr[b].y;
    arr[b].x = x;
    arr[b].y = y;
}

int Partition(Node *arr, int p, int r){
    int median_idx = FindMedianIndex(arr, p, (p+r)/2, r);
    Swap(arr, median_idx, r);
    int i = p - 1;
    for(int j = p ; j < r; j++){
        if(arr[r].x > arr[j].x){
            i++;
            Swap(arr, i, j);
        }
        else if(arr[r].x == arr[j].x){
            if(arr[r].y > arr[j].y){
                i++;
                Swap(arr, i, j);
            }
        }
    }
    i++;
    Swap(arr, i,r);
    return i;
}

void QuickSort(Node *arr, int p, int r){
    if(p<r){
        int q = Partition(arr, p, r);
        QuickSort(arr, p , q-1);
        QuickSort(arr, q+1, r);
    }
}

void PrintArr(Node *arr, int len){
    for(int i = 0 ; i < len; i++){
        printf("%d %d\n", arr[i].x, arr[i].y);
    }
}

int main(){
    //FILE  *fp = fopen("11650.txt", "r");
    FILE *fp = stdin;
    int num;
    fscanf(fp, "%d", &num);

    Node *arr = (Node*)(malloc(sizeof(Node)*num));
    for(int i = 0 ; i < num; i++){
        fscanf(fp, "%d%d", &(arr[i].x), &(arr[i].y));
    }
    QuickSort(arr, 0, num-1);
    PrintArr(arr, num);
    return 0;
}