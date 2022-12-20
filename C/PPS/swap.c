#include<stdio.h>

int main(){
    int num1 = 20, num2 = 30;

    printf("Numbers before swaping\n");
    printf("Num1 %d     Num2 %d \n", num1, num2);


    num1 = num1+num2;

    num2 = num1-num2;
    num1 = num1-num2;

    printf("Numbers after swaping\n");
    printf("Num1 %d     Num2 %d \n", num1, num2);
    
    return 0;
}