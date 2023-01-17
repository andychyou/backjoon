#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    char str[101];
    scanf("%s", str);
    int i = 0;
    int cnt = 0;
    int len = strlen(str);
    while(i < strlen(str)){
        if(str[i] == 'c'){
            if(str[i+1] == '-' || str[i+1] == '='){
                i += 2;
            }
            else i++;
        }
        else if(str[i] == 'd'){
            if(str[i+1] == '-'){ 
                i += 2;
            }
            else if(str[i+1] == 'z' && str[i+2] == '='){
                i += 3;
            }
            else i++;
        }
        else if(str[i] == 'l' && str[i+1] == 'j'){
            i += 2;
        }
        else if(str[i] == 'n' && str[i+1] == 'j'){
            i += 2;
        }
        else if(str[i] == 's' && str[i+1] == '='){
            i += 2;
        }
        else if(str[i] == 'z' && str[i+1] == '='){
            i += 2;
        }
        else{
            i++;
        }
        cnt++;
    }
    printf("%d", cnt); 
    return 0;


}

