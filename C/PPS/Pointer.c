#include<stdio.h>
int main(){
    int a = 5, *b;
    a = &b;

    printf("Value of a = %d\n", a);
    printf("Address of a = %u \n",b);
    printf("Value of a = %d \n", *b);
}