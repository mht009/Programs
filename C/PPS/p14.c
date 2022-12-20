#include<stdio.h>
void main()
{
int x,y,z;
y=2;
x=2;
x=2*(y++);
z=2*(++y);

printf("\n x=%d y=%d z=%d",x,y,z);

}