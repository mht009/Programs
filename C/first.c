#include<stdio.h>
void main(){
    int k =89, m = 74;
    int z = k <m ? k++ : m++;

    printf("%d",z);
}