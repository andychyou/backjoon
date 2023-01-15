#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int val;
    int cnt;
    struct node *lc;
    struct node *rc;
}Node;


Node* root;

void Find(Node* curr, Node** found_node, int* v){
    if(curr){
        Find(curr->lc, found_node, v);
        if(curr->val == *v){
            *found_node = curr;
        }
        Find(curr->rc, found_node, v);
    }
}

void Insert_Node(Node* curr, Node* newnode, Node* parent, int* insert_left){
    
    if(curr){
        if(curr->val < newnode->val){
            *insert_left = 0;
            Insert_Node(curr->rc, newnode, curr, insert_left);
        }
        else if(curr->val > newnode->val){
            *insert_left = 1;
            Insert_Node(curr->lc, newnode, curr, insert_left);
        }
    }
        
	else {
		if(root == NULL)
			root = newnode;
        else{
            if(*insert_left){
                parent->lc = newnode;
            }
            else{
                parent->rc = newnode;
            }
        }
	}
}


void Find_K(Node* curr, int k, int* cnt, int* cutline, int* found){
   if(curr){
       Find_K(curr->rc, k, cnt, cutline, found);
		int next_cnt = *cnt + curr->cnt;
		if(k > *cnt && k <= next_cnt){
            *cutline = curr->val;
        }
		*cnt = next_cnt;
       Find_K(curr->lc, k, cnt, cutline, found);
   }
}

// void Find_K(Node* curr, int k, int* cnt, int* cutline, int* found) {
// 	if (curr) {
// 		Find_K(curr->rc, k, cnt, cutline, found);
// 		if (*found == 0) {
// 			for (int i = 0; i < curr->cnt; i++) {
// 				*cnt += 1;
// 				if (*cnt == k) {
// 					*found = 1;
// 					*cutline = curr->val;
// 				}
// 			}
// 		}
	
// 		Find_K(curr->lc, k, cnt, cutline, found);
// 	}
// }

void Init_BST(FILE *fp, int N){
    root = NULL;
    int v;
    for(int i =0 ; i<N;i++){
        fscanf(fp, "%d", &v);
        //넣기 전에 해당 값이 있는지 확인. 있으면 해당 노드의 val 값을 증가
        Node* found_node = NULL;
        Find(root, &found_node, &v); 
        if(found_node){
           found_node->cnt += 1; 
        }
        else{
            Node* newnode = (Node*)malloc(sizeof(Node));
            newnode->cnt = 1;
            newnode->val = v;
            newnode->lc = newnode->rc = NULL;
            Node* parent = root;
			int insert_left = 0;
            Insert_Node(root,  newnode, parent, &insert_left);
        }
    }
    
}

void PrintSort(Node* curr) {
	if (curr) {
		PrintSort(curr->rc);
		printf("%d ", curr->val);
		PrintSort(curr->lc);
	}
}


int main(){
    //FILE *fp = fopen("25305.txt", "r");
	FILE *fp = stdin;
    int N, k;
    fscanf(fp, "%d %d", &N, &k);
    Init_BST(fp, N);
	//PrintSort(root);
    //printf("\n");
	int cnt = 0;
	int cutline = root->val;
	int found = 0;
    Find_K(root, k, &cnt, &cutline, &found);
    printf("%d", cutline);
    return 0;
}