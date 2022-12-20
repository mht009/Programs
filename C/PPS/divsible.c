/*Write a C program to find numbers between 1 to 200 not divisible by 13, 17 and 19*/

#include<stdio.h>

int main(){
    int i;

    printf("Numbers between 1 and 200 not divisible by 13, 17 and 19 are\n");
    for(i=1; i<=200; i++){
        if(i%13!= 0 && i%17!=0 && i%19!=0){
            printf("%d ",i);
        }
    }
}