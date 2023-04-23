'''creating a binary search tree'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def store_inorder(root, inorder):
    if root is None:
        return
    store_inorder(root.left, inorder)
    inorder.append(root.data)
    store_inorder(root.right, inorder)

def countNodes(root):
    if root is None:
        return 0
    return countNodes(root.left) + countNodes(root.right) + 1

def array_to_bst (arr, root):
    if root is None:
        return
    array_to_bst(arr, root.left)
    root.data = arr[0]
    arr.pop(0)

    array_to_bst(arr, root.right)

def binary_tree_to_bst(root):
    if root is None:
        return
    n = countNodes(root)
    arr = []
    store_inorder(root, arr)
    arr.sort()
    array_to_bst(arr, root)

def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.data, end=" ")
    print_inorder(root.right)