#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

//#define clrscr();

void clrscr();

//clrscr();

void main() 
{
    int a = 18, b = 9, c, d, e = 10, f;
    //system("cls");
    clrscr();
    c = b++;
    d = b; 
    f = a > b > d < c ;

    printf("%d", a < b < c > d);
    printf("%d", b == e);
    printf("%d", c + 1 > e);
    printf("%d", a + c == b > e < c + d);
    printf("%d", f != 1);
    printf("%d", a + c == b >= e < c + d != 1 );
}

void clrscr()
{
    system("cls");
}