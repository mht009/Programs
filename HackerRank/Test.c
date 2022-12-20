#include <stdio.h>
#include <stdlib.h>
#define Max 5

int x;

struct Queue
{
    int front;
    int rear;
    int arr[Max];
} que;

void insert()
{
    if (que.front == -1 && que.rear == -1)
    {
        printf("Enter number to insert: ");
        scanf("%d", &x);
        que.front = 0;
        que.rear = 0;

        que.arr[que.rear] = x;
    }
    else if (que.rear < Max - 1)
    {
        printf("Enter number to insert: ");
        scanf("%d", &x);
        que.rear++;
        que.arr[que.rear] = x;
    }
    else
    {
        printf("Queue Overflow\n\n");
    }
}

void delete ()
{
    if ((que.front == -1 && que.rear == -1) || (que.front < 0) || (que.front == que.rear + 1))
    {
        printf("Queue Underflow\n\n");
    }
    else
    {
        printf("%d is Deleted \n", que.arr[que.front]);
        que.front++;
    }
}

void print()
{
    if ((que.front == -1 && que.rear == -1) || (que.front < 0) || (que.front == que.rear + 1))
    {
        printf("Queue is\tEmpty\n\n");
    }
    else
    {
        printf("Queue is :\t");
        for (int i = que.front; i <= que.rear; i++)
        {
            printf("%d  ", que.arr[i]);
        }
        printf("\n");
    }
}

void main()
{
    int x;
    char op;
    que.front = -1;
    que.rear = -1;
    while (1)
    {
        printf("Enter operation 1 to push, 2 to pop : ");
        scanf(" %c", &op);

        switch (op)
        {
        case '1':
            insert();
            print();
            break;

        case '2':
            delete ();
            print();
            break;

        case '3':
            printf("Exit\n");
            exit(0);
            break;

        default:
            print("Invalid Input\n");
        }
    }
}