//다른 환경에서 빌드 및 테스트 진행 

#include <stdio.h>
#include <stdlib.h>

//Node 구조체 선언
typedef struct Node
{
    int key;
    struct Node* right, *left;
} Node;

//newNode 만들기 
//Insert 구현 
Node* insert(Node* node, int data){
    if (node==NULL){
        Node* node = (Node*)malloc(sizeof(Node));
        node->key=data;
        node->left = node->right = NULL;
        return node;
    }
    else{
        if (node->key>data){
            //node, data로 실수했더니 메모리 초과
            node->left=insert(node->left, data);
        }
        else{
            node->right=insert(node->right, data);
        }
    }
    return node;
}
//후위 순회 구현
void postOrder(Node* node){
    //return 뒤에 ;빠뜨렸더니 런타임 에러 (AccessNullPointer)
    if (node==NULL) return;
    postOrder(node->left);
    postOrder(node->right);
    printf("%d\n", node->key);
}

int main(){
    int data;
    Node* root = NULL;
    while(scanf("%d", &data) !=EOF){
        root=insert(root, data);
    }
    postOrder(root);
}