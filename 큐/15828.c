#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    int val;
    struct node *next;
}Node;

Node *front, *back;
int cur_size = 0;

void Push(int n){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = n;
    newnode->next = NULL;

    if (front == NULL){
        back = front = newnode;
    }
    else{
        back->next = newnode;
        back = newnode;
    }
	cur_size++;
}

int Pop(){
    int result = -1;
    if(front != NULL){
        result = front->val;
		Node* next = front->next;
        free(front);
        front = next;
    }
    cur_size--;
	return result;
}

int IsFull(int size){
    int result;
    result = (cur_size >= size) ? 1 : 0;
    return result;
}

int IsEmpty(){
    int result;
    result = (front == NULL) ? 1 : 0;
    return result;
}

void PrintQueue(){
    if(IsEmpty()) printf("empty");
    else{
        Node* curr = front;
        while(curr != NULL){
            printf("%d ", curr->val);
            curr = curr->next;
        }
    }
}

int main(){
    FILE *fp_in = fopen("15828test.txt", "r");
    int size;
    fscanf(stdin, "%d", &size);
    int in;
    while(1){
        fscanf(stdin, "%d", &in);
        if(in > 0){
            if(IsFull(size)){
                continue;
            }
            else{
                Push(in);
            }
        }
        else if(in == 0){
            Pop();
        }
		else {
			break;
		}
	}
    PrintQueue();
    return 0;
}