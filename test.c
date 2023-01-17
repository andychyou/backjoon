#include <stdio.h>

int main(){


int x,y;
char str[50];
scanf("%d ", &x);
fgets(str, 50, stdin);
printf("x = %d, str = %s", x, str);
return 0;


}

//https://www.codingninjas.com/codestudio/library/solved-the-problem-with-using-fgets-after-scanf
