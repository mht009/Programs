#include<stdio.h>
int main(){
/*
    printf("getchar() and putchar() function\n");
    char c;
    printf("\nEnter any character: \n");
    c = getchar();
    printf("Enterred character is \n");
    putchar(c);
*/

    printf("gets() and puts() function\n");
    char s[15];
    printf("\nEnter your name: ");
    gets(s);
    printf("your name is ");
    puts(s);


    return 0;
}