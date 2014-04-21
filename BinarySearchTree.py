class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val
        
    def insert(root,node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.left_child == None:
                    root.left_child = node
                else:
                    insert(root.left_child, node)
            else:
                if root.right_child == None:
                    root.right_child = node
                else:
                    insert(root.right_child, node)
    
    def delete(root,node):
        if root is None:
            return false
        else:
            if root.data > node.data:
                if root.left_child == None:
                    return false
                else:
                    delete(root.left_child, node)
            elif root.data < node.data:
                if root.right_child == None:
                    return false
                else:
                    delete(root.right_child, node)
            else:
                if(root.left_child is None and root.right_child is None):
                    root = None
                    return true
                elif (root.left_child is None and root.right_child is not None):
                    to_replace = find_smallest(root.right_child)
                    #I gotta give the tuple unpacking some credits, so damn easy
                    root.data, to_replace.data = to_replace.data, root.data
                    to_replace = None
                    return true
                else:
                    to_replace = find_smallest(root.left_child)
                    root.data, to_replace.data = toreplace.data, root.data
                    to_replace = None
                    return true
                    
    #The one to replace/swap is always the left child or the smallest of right sub tree            
    def find_smallest(root):
        if root is None:
            return None
        else:
            if root.left_child is not None:
                return find_smallest(root.left_child)
            else:
                return root

    def search(root,node):
        if root is None:
            return None
        else:
            if (root.data > node.data):
                search(root.left_child, node)
            elif (root.data < node.data):
                search(root.right_child,node)
            else:
                return root
