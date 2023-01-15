#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    int val;
    struct node *next;
}Node;

Node *front, *back;
int size = 0;

void Push_Front(int X){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = X;
    newnode->next = front;
    if(front == NULL){
        front = back = newnode;
        newnode->next = front;
    }
    else{
        back->next = newnode;
        front = newnode;
    }
    size++;
}

void Push_Back(int X){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = X;
    newnode->next = front;
    if(front == NULL){
        front = back = newnode;
        newnode->next = front;
    }
    else{
        back->next = newnode;
        back = newnode;
    }
    size++;
}

int Pop_Front(){
    if(Empty()){
        return -1;
    }
    Node* new_front = front->next;
    int result = front->val;
    free(front);
    front = new_front;
	size--;
    if(size == 0){
        front = back = NULL;
    }
    
    return result;
}


int Pop_Back(){
    if(Empty()){
        return -1;
    }
    Node* curr = front;
    Node* new_back = curr;
    while(curr != back){
        new_back = curr;
        curr = curr->next;
    }
    int result = back->val;
    free(back);
    back = new_back;
	size--;
    if(size == 0){
        front = back = NULL;
    }
    
    return result;
}

int Size(){
    return size;
}

int Empty(){
    if(front == NULL){
        return 1;
    }
    else return 0;
}

int Front() {
	int result = -1;
	if (front != NULL) {
		result = front->val;
	}
	return result;
}

int Back() {
	int result = -1;
	if (back != NULL) {
		result = back->val;
	}
	return result;
}

void FindCommand(FILE *fp, char* command){
    int n;
    if(!strcmp(command, "push_front")){
        fscanf(fp, "%d", &n);
        Push_Front(n);
    }
    else if (!strcmp(command, "push_back")){
        fscanf(fp, "%d", &n);
        Push_Back(n);
    }
    else if (!strcmp(command, "pop_front")){
        int val = Pop_Front();
		printf("%d\n", val);
    }
    else if (!strcmp(command, "pop_back")){
        int val = Pop_Back();
		printf("%d\n", val);
    }
    else if(!strcmp(command, "size")){
        printf("%d\n", Size());
    }
    else if(!strcmp(command, "empty")){
        printf("%d\n", Empty());
    }
    else if(!strcmp(command, "front")){
        printf("%d\n", Front());
    }
    else {
        printf("%d\n", Back());
    }
}


int main(){
    //FILE *fp = fopen("10866.txt", "r");
	FILE *fp = stdin;
    int n;
    char command[20];
    fscanf(fp, "%d", &n);
	for (int i = 0; i < n; i++) {
		fscanf(fp, "%s", command);
		FindCommand(fp, command);
	}
    
    return 0;
}