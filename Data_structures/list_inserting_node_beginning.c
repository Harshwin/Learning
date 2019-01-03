//INSERTION OF NODES AT THE BEGINNING OF A LIST

#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

struct Node {
    int data;
    struct Node* next;
}Node;

struct Node* head;
void Insert(int x)
{
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = head;
    head = temp; 

}

void print()
{
    //
    struct Node* temp = head;
    printf("the list is \n");
    while(temp!=0)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
}
int main()
{
    head = 0; // empty list;
    printf("how many numbers? \n");
    int n, i,x;
    scanf("%d",&n);
    for(i=0;i<n; i++){
        printf("\n enter the number \n");
        scanf("%d",&x);
        Insert(x);
        print();


    }

}