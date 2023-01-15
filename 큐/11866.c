#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int val;
    struct node *next;
    
}Node;

Node *front, *back, *curr;
int q_size = 0;
void Push(int n){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = n;
    newnode->next = front;

    if(front == NULL){
        front = back = newnode;        
    }
    else{
        back->next = newnode;
        back = newnode;
    }
    q_size++;
}

int Remove(Node* past){
    int result = curr->val;
	Node* future = curr->next;
    free(curr);
    curr = future;
	past->next = curr;
    q_size--;
    return result;
}

int main(){
    int N, K;
    front = back = curr = NULL;
    scanf("%d %d", &N, &K);
    for(int i = 1; i <= N; i++){
        Push(i);
    }
    Node *past = front;
    curr = front;
    printf("<");
    while(q_size > 0){
        for(int i = 0 ; i < K-1; i++){
            past = curr;
            curr=curr->next;
        }
        int re = Remove(past);
        printf("%d", re);
        if(q_size > 0){
            printf(", ");
        }
    }
    printf(">");
    return 0;
}