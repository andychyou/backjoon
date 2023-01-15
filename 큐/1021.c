#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int val;
    struct node *next;
    struct node *before;
}Node;

Node *front, *back;
int size = 0;



void Push(int i){
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->val = i;
    newnode->next = front;
    newnode->before = back;
    if(front == NULL){
        front = back = newnode;
        front->next = front;
        front->before = back;
    }
    else{
        back->next = newnode;
		back = newnode;
        front->before = newnode;
    }
    size++;
}

int Pop(){
    if(size == 0) return -1;
    int result = front->val;
    Node* new_front = front->next;
    free(front);
    front = new_front;
    back->next = front;
    front->before = back;
	size--;
    return result; 
}
void InitQueue(int len){
    front = back = NULL;
    for(int i = 1; i <= len; i++){
        Push(i);
    }
}
int Calc(int val){
    int cnt1 = 0;
	int cnt2 = 0;
 
	Node* curr1 = front;
	Node* curr2 = front;
    
    while(curr1->val != val){
        curr1 = curr1->next;
        cnt1++;
    }
    
    
    while(curr2->val != val){
        curr2 = curr2->before;
        cnt2++;
    }

	if (cnt1 < cnt2) {
		front = curr1;
		back = curr1->before;
	}
	else {
		front = curr2;
		back = curr2->before;
		cnt1 = cnt2;
	}
   
	
	Pop();
    return cnt1;
}


int main(){
    //FILE *fp = fopen("1021.txt", "r");
	FILE *fp = stdin;
    int len, n;
    fscanf(fp, "%d %d", &len, &n);
    InitQueue(len);
	int total = 0;
    for(int i = 0; i < n; i++){
        int val;
        fscanf(fp, "%d", &val);
        total += Calc(val);
        
    }
	printf("%d\n", total);
    return 0;
}