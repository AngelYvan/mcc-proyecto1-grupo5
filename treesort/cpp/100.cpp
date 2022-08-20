#include <vector>
#include <iostream>
using namespace std;
struct Node
{
  int data;
  struct Node *left,*right;
};
//Function to create new Node
struct Node *newnode(int key)
{
  struct Node *temp=new Node;
  temp->data=key;
  temp->left=NULL;
  temp->right=NULL;
  return temp;
}
Node* insert(Node *node,int key)
{
  if(node==NULL) return newnode(key);//If tree is empty return new node
  if(key < node->data)
    node->left=insert(node->left,key);
  else
    node->right=insert(node->right,key);
  return node;
}
void store(Node *root,int a[],int &i)
{
  if(root!=NULL)
  {
    store(root->left,a,i);
    a[i++]=root->data;
    store(root->right,a,i);
  }
}
void TreeSort(vector<int>& a)
{
    struct Node *root = NULL;
    //Construct binary search tree
    root = insert(root, a[0]);
    for (size_t i=1; i<a.size(); i++)
        insert(root, a[i]);
    //Sorting the array using inorder traversal on BST
    int i = 0;
    store(root, a.data() , i);
}
int main()
{ 
    vector<int> a{21,2,61,63,50,35,46,42,3,80,14,80,7,65,27,32,23,7,4,72,96,37,10,87,60,61,46,38,85,77,99,38,54,93,35,28,19,52,100,62,67,71,85,78,57,27,45,20,61,22,11,70,100,79,74,27,64,82,7,56,15,73,68,13,30,39,34,94,17,70,32,37,49,34,51,56,3,91,77,62,56,65,98,92,61,75,11,91,35,54,63,16,24,22,11,28,43,15,4,53
};
    TreeSort(a); 
    cout<<"The sorted array is :\n";
    //Printing the sorted array
    for(size_t i=0;i<a.size();i++)
    {
      cout<<a[i]<<" ";
    }
    return 0;
}