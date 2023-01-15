#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    int val;
    struct node *next;
}Node;

Node *front = NULL;
Node *back = NULL;

void InitQueue(int n);
void Push(int n);
int Pop();
int Empty();
int Cal(int n);

int main(){
    int num;
    fscanf(stdin, "%d", &num);
    InitQueue(num);
    int result = Cal(num);
    printf("%d", result);
    return 0;
}

void InitQueue(int n){
    // if(n <= 0){
    //     return;
    // }
    // front = (Node*)malloc(sizeof(Node));
    // front->val = 1;
    // front->next = NULL;
    // back = front;
    // for(int i = 2; i <= n; i++){
    //    Node* newnode = (Node*)malloc(sizeof(Node));
    //    newnode->val = i;
    //    newnode->next = NULL;
    //    back->next = newnode;
    //    back = newnode;
    // }
    for(int i = 1 ; i <= n; i++){
        Push(i);
    }
}

void Push(int n){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = n; 
    newnode->next = NULL;
    if (front == back && front == NULL){
        front = back = newnode;
    }
    else{
        back->next = newnode;
        back = newnode;
    }
}

int Pop(){
    int return_val = front->val;
    Node* temp = front->next;
    free(front); 
    if(temp == NULL){
        front = back = NULL;
    }
    // front가 free하면서 *fron, result 값들이 바뀜에 따라 front->next 값도 ???로 바뀐다
    // 그렇기 때문에 front->next == NULL을 보장할 수 없다 
    // 근데 temp = front->next로 미리 temp에 값을 저장한 다음 free(front)를 하면
    // temp 값에는 이미 front->next였던 값이 저장되고 이건 free(front)해도 temp 값의 영향을 주지 않는다다
	// if (front->next == NULL) {
	// 	front = back = NULL;
	// }
    else{
        front = temp;
    }
    return return_val;
}

int Empty(){
    int return_val;
    if(front == NULL && back == NULL){
        return_val = 1; 
    }
    else{
        return_val = 0;
    }
    return return_val;
}

int Cal(int n){
    int result = -1;
    while(1){
        result = Pop();
        if(Empty()) break;
        result = Pop();
        Push(result);
    }
    return result;
}