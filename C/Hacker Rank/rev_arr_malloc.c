#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr1, i, *arr;
    scanf("%d", &num);
    arr1 = (int *)malloc(num * sizeof(int));
    for (i = 0; i < num; i++)
    {
        scanf("%d", arr1 + i);
    }

    arr = (int *)malloc(num * sizeof(int));
    int count = num - 1;

    for (int j = 0; j < num; j++)
    {
        arr[j] = arr1[count--];
    }

    for (i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}