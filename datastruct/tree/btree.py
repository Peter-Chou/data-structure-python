# -*- coding: utf-8 -*-


class BinaryTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """build from

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = dict()
        for node_data in node_list:
            data = node_data["data"]
            node_dict[data] = BinaryTreeNode(data)  # 只有data被赋值

        for node_data in node_list:
            data = node_data["data"]
            node = node_dict[data]  # 得到 data对应的BinaryTreeNode
            if node_data["is_root"]:
                root = node
            node.left = node_dict.get(node_data["left"])    # node左边指向一个node
            node.right = node_dict.get(node_data["right"])
        return cls(root)    # 设置self.root节点，并返回作为树的入口

    def preorder_trav(self, subtree):
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


if __name__ == "__main__":
    node_list = [
        {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False},
    ]

    btree = BinaryTree.build_from(node_list)
    btree.preorder_trav(btree.root)
    btree.reverse(btree.root)
    print("=====after reverse tree=====")
    btree.preorder_trav(btree.root)
