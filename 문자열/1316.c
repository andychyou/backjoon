#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int IsGroup(char *str){
    char is_char[26] = {0,};
    int is_group = 1;
    for(int i = 0 ; i < strlen(str); i++){
        if(is_char[str[i] - 'a'] == 0){
           is_char[str[i] - 'a'] = 1; 
        }
        else{
            if(str[i-1] != str[i]){
                is_group = 0;
                break;
            }
        }
    }
    return is_group;
}


int main(){
    FILE *fp = stdin;
    int n;
    fscanf(fp, "%d", &n);
    char s[101];
    int total = 0;
    for(int i = 0 ; i < n;i++){
        fscanf(fp, "%s", s);
        total += IsGroup(s);
    }
    printf("%d", total);
    return 0;
}