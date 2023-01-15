//bst를 만들어 inorder로 트리 노드의 개수 / 2 + 1 번째 탐색일 때가 median인 것을 이용
//같은 값이 있는 노드가 있을 수 있기 때문에 node의 cnt 값이 해당 값의 빈도수를 나타냄


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define LINE 5

typedef struct node{
    int val;
    int cnt;
    struct node *lc;
    struct node *rc;
}Node;

Node* root;

//n값이 tree에 있는지 없는지 확인
Node* Find(int n){
    Node* found_node = NULL;
    
    if(root == NULL) found_node = NULL;
    else{
       Node* curr = root;
       while(curr != NULL){
            if(curr->val < n){
                curr = curr->rc;
            }
            else if(curr->val > n){
                curr = curr->lc;
            }
            else{
                found_node = curr;
                break;
            }
       }
    }
    return found_node;
}

void Inorder(int *cnt, Node* curr, int* median){
    if(curr){
        Inorder(cnt, curr->lc, median);
		for (int i = 0; i < curr->cnt; i++) {
			*cnt += 1;
			if (*cnt == LINE / 2 + 1) {
				*median = curr->val;
			}
		}
        
        Inorder(cnt, curr->rc, median);
    }
}


void Add_Tree(Node* newnode){
    if(root == NULL){
        root = newnode;
        return;
    }
    Node* curr = root;
    Node* parent = curr;
    int add_left;
    while (curr != NULL)
    {
        parent = curr;
        if(curr->val < newnode->val){
            curr = curr->rc;
            add_left = 0;
        }
        else if(curr->val > newnode->val){
            curr = curr->lc;
            add_left = 1;
        }
    }
    
    if(add_left){
        parent->lc = newnode;
    }
    else{
        parent->rc = newnode;
    }
}

int main(){
    //FILE *fp = fopen("2587.txt", "r");
	FILE *fp = stdin;
    root = NULL;
    int val;
    int mean = 0;
    int median;
    for(int i = 0; i < LINE; i++){
        fscanf(fp, "%d", &val);
        mean += val;
        Node* found_node = Find(val);
        if(found_node != NULL){
            found_node->cnt += 1;
        }
        else{
            Node* newnode = (Node*)malloc(sizeof(Node));
            newnode->val = val;
            newnode->cnt = 1;
            newnode->lc = newnode->rc = NULL;
            Add_Tree(newnode);
        } 
        
    }
    mean /= LINE;
	int c = 0;
    Inorder(&c, root, &median);
    printf("%d\n%d", mean, median);
    return 0;
}