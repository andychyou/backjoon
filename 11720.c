#include <stdlib.h>
#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    char c;
    int sum = 0;
    for(int i = 0 ; i < n; i++){
        scanf("%c", &c);
        printf("%c0", c);
        c = c - '0';
        sum += c;
    }
    printf("%d", sum);
}


