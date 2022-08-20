class Node:
 
  def __init__(self,item = 0):
    self.key = item
    self.left,self.right = None,None
 
 
# Root of BST
root = Node() 
root = None
 
# This method mainly
# calls insertRec()
def insert(key):
  global root
  root = insertRec(root, key)
 
# A recursive function to
# insert a new key in BST
def insertRec(root, key):
 
  # If the tree is empty,
  # return a new node
 
  if (root == None):
    root = Node(key)
    return root
 
  # Otherwise, recur
  # down the tree
  if (key < root.key):
    root.left = insertRec(root.left, key)
  elif (key > root.key):
    root.right = insertRec(root.right, key)
 
  # return the root
  return root
 
# A function to do
# inorder traversal of BST
def inorderRec(root):
  if (root != None):
    inorderRec(root.left)
    print(root.key ,end = " ")
    inorderRec(root.right)
   
def treeins(arr):
  for i in range(len(arr)):
    insert(arr[i])
 
# Driver Code
arr = [21,2,61,63,50,35,46,42,3,80,14,80,7,65,27,32,23,7,4,72,96,37,10,87,60,61,46,38,85,77,99,38,54,93,35,28,19,52,100,62,67,71,85,78,57,27,45,20,61,22,11,70,100,79,74,27,64,82,7,56,15,73,68,13,30,39,34,94,17,70,32,37,49,34,51,56,3,91,77,62,56,65,98,92,61,75,11,91,35,54,63,16,24,22,11,28,43,15,4,53]

treeins(arr)
inorderRec(root)
