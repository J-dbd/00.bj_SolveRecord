//다른 환경에서 빌드 및 테스트 진행 //메모리 초과가 남

#include <stdio.h>
#include <stdlib.h>

//Node 구조체 선언
typedef struct Node
{
    int key;
    struct Node* right, *left;
} Node;

//newNode 만들기 
Node* newNode(int data){
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->key=data;
    temp->right=NULL;
    temp->left=NULL;
    return temp;
}


//Insert 구현 
Node* insert(Node* node, int data){
    if (node==NULL){
        return newNode(data);
    }
    else{
        if (node->key>data){
            node->left=insert(node, data);
        }
        else{
            node->right=insert(node, data);
        }
    }
    return node;
}
//후위 순회 구현
void postOrder(Node* node){
    if (node!=NULL){
        postOrder(node->left);
        postOrder(node->right);
        printf("%d", node->key);
    }
    return;
}

int main(){
    int data;
    Node* root = NULL;
    while(scanf("%d", &data) !=EOF){
        root=insert(root, data);
    }
    postOrder(root);
}