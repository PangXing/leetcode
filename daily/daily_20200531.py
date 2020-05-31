# coding:utf-8

'''
【101】对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
进阶：
你可以运用递归和迭代两种方法解决这个问题吗？
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CompeleteTree(object):
    def __init__(self, tree_list):
        if not tree_list:
            self.root = None
        else:

            self.root = TreeNode(tree_list[0])
            queue = list()
            queue.append(self.root)
            index = 0
            index1 = 1
            while index1 < len(tree_list):
                root = queue[index]
                root.left = TreeNode(tree_list[index1])
                index1 += 1
                queue.append(root.left)
                root.right = TreeNode(tree_list[index1])
                index1 += 1
                queue.append(root.right)
                index += 1

class Solution(object):
    '''
    如果同时满足下面的条件，两个树互为镜像：
        1.它们的两个根结点具有相同的值
        2.每个树的右子树都与另一个树的左子树镜像对称
    '''
    def isSymmtricSubTree(self, left, right):
        flag = False
        if left is None and right is None:
            flag = True
        elif left and right:
            if left.val == right.val:
                flag_1 = self.isSymmtricSubTree(left.left, right.right)
                flag_2 = self.isSymmtricSubTree(left.right, right.left)
                if flag_1 and flag_2:
                    flag = True
        return flag


    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmtricSubTree(root.left, root.right)

if __name__ == '__main__':
    solution = Solution()
    tree_list = [1, 2, 2, 3, 4, 4, 3]
    tree = CompeleteTree(tree_list)
    print solution.isSymmetric(tree.root)
    tree_list = [1, 2, 2, None, 3, None, 3]
    tree = CompeleteTree(tree_list)
    print solution.isSymmetric(tree.root)


