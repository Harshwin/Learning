#include<stdlib.h>
#include<stdio.h>

struct Node {
    int data;
    struct Node* next;

};
struct Node* head;

void Print(){
    Node* temp = head;
    printf("\n");
    while(temp != 0){
        printf("%d",temp->data);
        temp = temp->next;

    }
    printf("\n");
}
void Insert(int data,int n){
    Node* temp1 = new Node();
    temp1->data = data;
    temp1->next = 0;
    if(n==1){
        temp1->next = head;
        head = temp1;
        //printf("\n temp1 value : %d",temp1);
        return;
    }
    Node* temp2 = head;
    for(int i=0; i<n-2; i++){
        temp2 = temp2->next;
        printf("inside : %d", temp2);
    }
    temp1->next = temp2->next;
    temp2->next = temp1;

}
int main(){
    head = 0; // empty list
    Insert(2,1);//List : 2
    Insert(3,2);//List : 2,3
    Insert(4,1);//List : 4,2,3
    Insert(5,2);//List : 4,5,2,3
    Insert(7,3);//List : 4,5,7,2,3

    Print();
}

