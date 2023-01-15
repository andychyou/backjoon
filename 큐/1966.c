#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int val;
    struct node *next;
}Node;

Node* front, *back, *curr;


void Push(int n){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = n;
    newnode->next = front;

    if(front == NULL){
        front = back = newnode;
        front->next = front;
    }
    else{
        back->next = newnode;
        back = newnode;
    }
}

int Pop(){
    int result = front->val;
    Node* temp = front->next;
    free(front);
    if(front == back){
        front = back = NULL;
    }
    else{
        front = temp;
        back->next = temp;
    }
    return result;
}

void InitQueue(FILE *fp, int n){
    front = back = curr = NULL;
    for(int j = 0; j < n; j++){
        int i;
        fscanf(fp, "%d", &i);
        Push(i);
    }
}

Node* FindTarget(int n){
    Node* target = front;
    for(int i = 0; i < n; i++){
        target = target->next;
    }
    return target;
}

int Calc(Node* target){
    int  cnt = 1;

    while(1){
        Node* og_front = front; 
        Node* curr = og_front;
        Node* before = back;
        int max = curr->val;
        do{
            if(curr->val > max){
                max = curr->val;
                front = curr;
                back = before;
            }
            before = curr;
            curr = curr->next;
        }while(curr != og_front);
        if(front == target){
            break;
        }
        else{
            Pop();
        }
        cnt++;
    }
	return cnt;
}

int main(){
	//FILE *fp = fopen("1966.txt", "r");
	FILE *fp = stdin;
    int T;
    fscanf(fp, "%d", &T);
    for(int i = 0; i < T; i++){
        int N, I;
        fscanf(fp, "%d %d", &N, &I);
        InitQueue(fp, N);
        Node* target = FindTarget(I);
        int re = Calc(target);
        printf("%d\n", re);
    }

    return 0;
}