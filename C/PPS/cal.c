
# include <stdio.h>
int main() {
char operator;
double fno,sno;
printf("Enter an operator (+, -, *, /): ");
scanf("%c", &operator);
printf("Enter two operands: ");
scanf("%lf %lf",&fno,&sno);
switch(operator)
{
case '+':
printf("%lf + %lf = %lf",fno, sno, fno+sno);
break;
case '-':
printf("%lf - %lf = %lf",fno, sno, fno-sno);
break;
case '*':
printf("%lf * %lf = %lf",fno, sno, fno*sno);
break;
case '/':
printf("%lf / %lf = %lf",fno, sno,fno/sno);
 break;
// operator is doesn't match any case constant (+, -, *, /)
default:
printf("Error! operator is not correct");
}
return 0;
}