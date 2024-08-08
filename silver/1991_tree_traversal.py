import sys
from collections import deque

"""
1. preorder traversal
2. inorder traversal
3. postorder traversal
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        # self.parent = parent


class BinaryTree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, value, left, right):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        if left != '.':
            if left not in self.nodes:
                self.nodes[left] = Node(left)
            self.nodes[value].left = self.nodes[left]
        if right != '.':
            if right not in self.nodes:
                self.nodes[right] = Node(right)
            self.nodes[value].right = self.nodes[right]
        if self.root is None:
            self.root = self.nodes[value]

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
        return result

    def postorder(self):
        return self._postorder(self.root, [])

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)
        return result


def build_tree_from_input(num, input_data):
    tree = BinaryTree()
    for i in range(num):
        value, left, right = input_data[i].split()
        tree.add_node(value, left, right)
    return tree


def main():
    num = int(sys.stdin.readline().strip())
    input_data = [sys.stdin.readline().strip() for _ in range(num)]
    tree = build_tree_from_input(num, input_data)
    print(''.join(tree.preorder()))
    print(''.join(tree.inorder()))
    print(''.join(tree.postorder()))


if __name__ == "__main__":
    main()
