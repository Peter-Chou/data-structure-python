# -*- coding: utf-8 -*-


class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict["key"]
            key_to_node_dict[key] = BSTNode(key, value=key)  # 暂时用value与key一样

        for node_dict in node_list:
            key = node_dict["key"]
            node = key_to_node_dict[key]
            if node_dict["is_root"]:
                root = node
            node.left = key_to_node_dict.get(node_dict["left"])
            node.right = key_to_node_dict.get(node_dict["right"])
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        """根据bst特性查找key
        """
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def __contains__(self, el):
        """实现in操作符
        """
        return self._bst_search(self.root, el) is not None

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:  # 找到左子树的头
            return subtree
        else
        return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        """插入并且返回根节点
        """
        if subtree is None:  # 如果root为空
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:    # 更新已经存在的key
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        """删除节点并返回根节点
        """
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        else:   # 找到了要删除的节点
            # 叶节点， 返回None 把其父亲指向它的指针指为None
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:  # 只有一个孩子
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:   # 两个孩子，寻找后继节点替换，删除右子树的后继节点&更新右子树
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(
                    subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)
