class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Function 1: Inverse Tree
# Write a function `inverse_tree(root)` that receives the root of a binary tree
# and makes the tree a mirror image of itself.
# Example:
# Input Tree:
#       1
#      / \
#     2   3
#
# Output Tree:
#       1
#      / \
#     3   2


def inverse_tree(root):
    if root:
        root.right, root.left = root.left, root.right
        inverse_tree(root.right)
        inverse_tree(root.left)


# Function 2: Boolean Mirror Trees
# Write a function `are_mirror_trees(root1, root2)` that receives two tree roots
# and returns `True` if the trees are mirror images of each other,
# and `False` otherwise.
# Example:
# Tree 1:
#       1
#      / \
#     2   3
#
# Tree 2:
#       1
#      / \
#     3   2
# Output: True


def are_mirror_trees(root1, root2):
    if bool(root1) != bool(root2):
        return False
    if root1 is None and root2 is None:
        return True
    return root1.key == root2.key and \
        are_mirror_trees(root1.left, root2.right) and \
        are_mirror_trees(root1.right, root2.left)


# Function 3: Longest Zigzag Path
# Write a function `longest_zigzag(root)` that receives the root of a binary tree
# and returns a list of keys along the longest zigzag path.
# A "zigzag" occurs when the path alternates directions (left -> right -> left or right -> left -> right).
# The alternations do not have to be in consecutive levels of the tree to be considered part of a zigzag.
# Example:
# Tree:
#         1
#        / \
#       2   3
#      / \    \
#     0   4     5
#        /     / \
#       6     12  7
#                 /
#                8
#               / \
#              6   9
#                   \
#                   17
#                   /
#                  10

# Longest Zigzag Path: [3, 5, 7, 8, 9, 17, 10]

def longest_zigzag(root, is_left_child=None):
    if not root:
        return -1, []

    left_length, left_path = longest_zigzag(root.left, is_left_child=True)
    right_length, right_path = longest_zigzag(root.right, is_left_child=False)

    if is_left_child:
        right_length += 1
    elif is_left_child is not None:
        left_length += 1
    return (left_length, [root.key] + left_path) if left_length >= right_length else (
    right_length, [root.key] + right_path)


# Function 4: Lowest Common Ancestor
# Write a function `lowest_common_ancestor(root, node1, node2)` that receives the root of a binary tree and two nodes.
# It should return the lowest common ancestor (LCA) of the two nodes.
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
#      / \
#     8   6
#        / \
#       7   10

# LCA of 8 and 10: 5
# LCA of 6 and 4: 2
# LCA of 7 and 3: 1


def bfs_search(root, node1, node2):
    q = []
    x = None
    if root:
        q.append(root)
        while q:
            x = q.pop(0)
            if x == node1 or x == node2:
                break
            if x != None:
                q.append(x.left)
                q.append(x.right)
    return x


def lowest_common_ancestor(root, node1, node2):
    if root == node1 or root == node2:
        return print("one of the given nodes is the parent of the other or isn't exist")

    x = bfs_search(root.left, node1, node2)
    y = bfs_search(root.right, node1, node2)

    if x == node1 and y == node2 or x == node2 and y == node1:
        return root.key
    elif x == node1 or x == node2:
        return lowest_common_ancestor(root.left, node1, node2)
    elif y == node1 or y == node2:
        return lowest_common_ancestor(root.right, node1, node2)
    return


# Function 5: Print Tree by Rows
# Write a function `print_tree_by_rows(root)` that prints the tree level by level using a breadth-first search (BFS).
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#
# Output:
# 1
# 2 3
# 4 5 6

def print_tree_by_rows(root):
    q = []
    q.append(root)
    while q:
        arr = []
        for i in range(len(q)):
            x = q.pop(0)
            arr.append(x.key)
            if x.left is not None:
                q.append(x.left)
            if x.right is not None:
                q.append(x.right)
        print(arr)


# Instructions for Writing Tests
# Write test cases for each of the above functions. For each test:
# - Provide an example input (tree or trees for comparison).
# - Include the expected output based on the provided examples.
# - Ensure that your tests cover various edge cases, such as empty trees, single-node trees, or trees with specific structures.
# You can use helper functions to build binary trees for testing.


# Recommendation:
# To visualize binary trees, you can use the `graphviz` library. It allows you to create graphical representations of trees
# and save them as image files. This can be especially useful for debugging and understanding tree structures.
# Example:
# 1. Install Graphviz:
#    pip install graphviz
# 2. Use the following function to visualize a binary tree:

from graphviz import Digraph


def visualize_tree(root, filename="tree"):
    def add_nodes_edges(node, dot=None):
        if node:
            dot.node(str(node.key), str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left, dot)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right, dot)

    dot = Digraph()
    add_nodes_edges(root, dot)
    dot.render(filename, format="png", cleanup=True)  # Save as PNG
    print(f"Tree visualization saved as {filename}.png")


# This will create an image of the binary tree structure for easy reference.
a = TreeNode(4)
b = TreeNode(5)

root1 = TreeNode(3, a, b)
visualize_tree(root1, "tree")

inverse_tree(root1)
visualize_tree(root1, "mirror_tree")

root2 = TreeNode(3, b, a)
visualize_tree(root2, "tree_2")
print("Are the trees a mirror image of each other?", are_mirror_trees(root1, root2))

a = TreeNode(10)
ab = TreeNode(90)
b = TreeNode(7, None, ab)
c = TreeNode(6, b, a)
d = TreeNode(8)
e = TreeNode(5, d, c)
f = TreeNode(4, )
g = TreeNode(3)
h = TreeNode(2, f, e)
root3 = TreeNode(1, h, g)
visualize_tree(root3, "tree_3")

print("The lowest common ancestor is:", lowest_common_ancestor(root3, a, ab))

print("The tree by rows is:")
print_tree_by_rows(root3)

print("The longest zigzag path is:", longest_zigzag(root3))
