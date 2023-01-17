#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *strrev(char *str)
{
    if (!str || ! *str)
        return str;

    int i = strlen(str) - 1, j = 0;

    char ch;
    while (i > j)
    {
        ch = str[i];
        str[i] = str[j];
        str[j] = ch;
        i--;
        j++;
    }
    return str;
}

int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    char str1[4], str2[4];
    sprintf(str1, "%d", a);
    sprintf(str2, "%d", b);
    strrev(str1);
    strrev(str2);
    a = atoi(str1);
    b = atoi(str2);
    a > b ? printf("%d", a) : printf("%d", b);
    return 0;
}