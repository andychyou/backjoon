#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    char str[16];
    scanf("%s", str);
    int time = 0;
    for(int i = 0 ; i < strlen(str); i++){
        if(str[i] >= 'P' && str[i] <= 'S'){
            time += 8;
        }
        else if(str[i] >= 'T' && str[i] <= 'V'){
            time += 9; 
        }
        else if(str[i] >= 'W' && str[i] <= 'Z'){
            time += 10; 
        }
        else{
            time += (str[i] - 'A') / 3 + 3;
        }
 
    }
    printf("%d", time);
    return 0;
}

