#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct _node{
	int val;
	struct _node *next;
}Node;
Node* front = NULL;
Node* back = NULL;
Node* real_back = NULL;
int size = 0;
void Queue_init();
void FindCommand(char* command, FILE* fp);
void Push(int i);
int Pop();
int Size();
int Empty();
int Front();
int Back();

int main(){
	Queue_init();
	//FILE* fp = fopen("test.txt", "r");
	FILE* fp = stdin;
	int args;
	fscanf(fp, "%d", &args);
	for(int i = 0 ; i < args; i++){
		char command[20];
		fscanf(fp, "%s", command);
		FindCommand(command, fp);
		
	}	
	return 0;
}

void Queue_init() {
	front = (Node*)malloc(sizeof(Node));
	back = real_back = front;
	back->val = -1;
	back->next = NULL;
}

void FindCommand(char* command, FILE* fp){
	if(!strcmp(command, "push")){
		int i;
		fscanf(fp, "%d", &i);
		Push(i);
	}
	else if(!strcmp(command, "pop")){
		int val = Pop();
		printf("%d\n", val);
	}
	else if(!strcmp(command, "size")){
		// int val = Size();
		int val = size;
		printf("%d\n", val);
	}
	else if(!strcmp(command, "empty")){
		int val = Empty();
		printf("%d\n", val);
	}
	else if(!strcmp(command, "front")){
		int val = Front();
		printf("%d\n", val);
	}
	else if(!strcmp(command, "back")){
		int val = Back();
		printf("%d\n", val);
	}
}

void Push(int i){
	if(Empty()){
		front->val = i;		
	}
	else{		
		back->val = i;
	}
	Node* newnode = (Node*)malloc(sizeof(Node));
	newnode->val = -1;
	newnode->next = NULL;
	real_back = back;
	back->next = newnode;
	back = newnode;
	size++;
}

int Pop(){
	if(Empty()) {
		size = 0;
		return -1;		
	}
	int return_val = front->val;
	Node* temp = front;
	front = front->next;
	free(temp);
	size--;
	return return_val;
}

int Size(){
	int size = 0;
	for(Node* temp = front; temp != NULL; temp = temp->next){
		if(temp->val > -1){
			size++;	

		}
	} 
	return size;
}

int Empty(){
	if(front == back){
		return 1;	
	}
	else return 0;
}

int Front(){
	if(Empty()) return -1;
	return front->val;
}

int Back(){
	if(Empty()) return -1;
	return real_back->val;
}

