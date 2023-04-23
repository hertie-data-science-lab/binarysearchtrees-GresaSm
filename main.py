
from binarysearchtree import Node, binary_tree_to_bst, print_inorder, store_inorder, countNodes, array_to_bst

'''testing the conversion of binary tree to binary search tree'''
root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(25)
print("Inorder traversal of the given tree")
print_inorder(root)

'''convert binary tree to binary search tree'''

binary_tree_to_bst(root)
print("Inorder traversal of the converted Binary Search Tree is:")
print_inorder(root)


