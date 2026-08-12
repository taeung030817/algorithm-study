class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(node, result=None):
    """왼쪽 자식 -> 현재 노드 -> 오른쪽 자식 순으로 순회."""
    if result is None:
        result = []
    if node is None:          # base case
        return result

    inorder(node.left, result)
    result.append(node.val)
    inorder(node.right, result)
    return result


if __name__ == "__main__":
    #      2
    #     / \
    #    1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(inorder(root))  # [1, 2, 3]
