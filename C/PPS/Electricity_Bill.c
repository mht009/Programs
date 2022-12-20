#include<stdio.h>

float main(){
    int in_r, fi_r, con;
    float amt;

    printf("Enter the initial reading: ");
    scanf("%d", &in_r);
    //printf("\n");
    printf("Enter th final reading: ");
    scanf("%d", &fi_r);
    //printf("\n");

    con = fi_r-in_r;

    if (con >=0 && con <= 200){
        amt = con * 3.45;
    }

    else if (con>=201 && con <=500){
        amt= con * 5.50;
    }
    else{
        amt = con * 6.70;
    }

    printf("Electricity bill : %f", amt);
}