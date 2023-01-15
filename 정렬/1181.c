#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SENT_LEN 51


int SentLen(char *sent){
    int i = 0;
    int len = 0;
    while(sent[i]){
        len++;
        i++;
    }
    //\0센거 빼기
    return len-1;
}

void Merge(char **arr1, char **arr2, int low, int mid, int high){
    int curr1, curr2, k;
    curr1 = low;
    curr2 = mid+1;
    k = low; 
    while(curr1 <= mid && curr2 <= high){
        if(SentLen(arr1[curr1]) < SentLen(arr1[curr2])){
            arr2[k] = arr1[curr1];
            curr1++;
        }
        else if (SentLen(arr1[curr1]) > SentLen(arr1[curr2])){
            arr2[k] = arr1[curr2];
            curr2++;
        }
        else{
            //알파벳 순서는 strcmp값이 작은 쪽이 더 빠름
            // strcmp는 -1, 0, 1 고정 값 말고 부등호로 판별해야함
            // switch (strcmp(arr1[curr1], arr1[curr2]))
            // {
            // case -1:
            //     arr2[k] = arr1[curr1];
            //     curr1++;
            //     break;
            // default:
            //     arr2[k] = arr1[curr2];
            //     curr2++;
            //     break;
            // }
            // strcmp는 -1, 0, 1 고정 값 말고 부등호로 판별해야함
            if (strcmp(arr1[curr1], arr1[curr2]) < 0){
                arr2[k] = arr1[curr1];
                curr1++;
            }
            else{
                arr2[k] = arr1[curr2];
                curr2++;
            }

            
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
    for(int i = low; i <= high; i++){
        //이건 되면서
        arr1[i] = arr2[i];
    }
}

void MergeSort(char **arr1, char **arr2, int low, int high){
    if(low < high){
        int mid = (low+high)/2;
        MergeSort(arr1, arr2, low, mid);
        MergeSort(arr1, arr2, mid+1, high);
        Merge(arr1, arr2, low, mid, high);
    }
}

void PrintArr(char **arr, int num){
    //왜 스택으로하면 안되냐
    char check_same[SENT_LEN];
    // check_same = "\0";
    // char *check_same = (char*)malloc(sizeof(char)*SENT_LEN);
    // check_same = "\0";
    printf("%s", arr[0]);
    strcpy(check_same, arr[0]);
    for(int i = 1; i < num; i++){
        if(strcmp(check_same, arr[i]) != 0){
            printf("\n%s", arr[i]);
        }
        //왜 이거 안되냐
        // check_same = arr[i];
        strncpy(check_same, arr[i], SENT_LEN); 
    }
}

void PrintArr(char **arr, int num){
    //스택 선언에서는 = 기호로 재할당이 안됨. strncpy로 복사해줘야 함
    char check_same[SENT_LEN];
    //check_same = "\0" 또는 check_same = arr[0] 안됨
    strncpy(check_same, "\0", SENT_LEN);
    printf("%s", arr[0]);
    strcpy(check_same, arr[0]);
    for(int i = 1; i < num; i++){
        if(strcmp(check_same, arr[i]) != 0){
            printf("\n%s", arr[i]);
        }
        strncpy(check_same, arr[i], SENT_LEN); 
    }
}

void PrintArr(char **arr, int num){
    //반면 heap로 선언했을 때는 = 로 재할당 가능. 
    char *check_same = (char*)malloc(sizeof(char)*SENT_LEN);
    check_same = "\0";
    //반대로 strcpy가 먹히지 않음
    //strcpy(check_same, arr[0]);
    for(int i = 1; i < num; i++){
        if(strcmp(check_same, arr[i]) != 0){
            printf("\n%s", arr[i]);
        }
        //왜 이거 안되냐
        // check_same = arr[i];
        strncpy(check_same, arr[i], SENT_LEN); 
    }
}

int main(){
    FILE *fp = fopen("1181.txt", "r");
    //FILE *fp = stdin;
    int num;
    fscanf(fp, "%d", &num);
    char **arr1 = (char**)malloc(sizeof(char*)*num);
    for(int i = 0 ; i < num; i++){
        arr1[i] = (char*)malloc(sizeof(char)*SENT_LEN);
    }
    char **arr2 = (char**)malloc(sizeof(char*)*num);
    for(int i = 0 ; i < num; i++){
        arr2[i] = (char*)malloc(sizeof(char)*SENT_LEN);
    }
    for(int i = 0; i < num; i++){
        fscanf(fp, "%s", arr1[i]);
    }
    MergeSort(arr1, arr2, 0, num-1);
    PrintArr(arr1, num);
    return 0;
}