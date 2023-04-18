class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
            print('DONE')
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val == node.val:
            print('ALREADY')
        elif val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
                print('DONE')
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
                print('DONE')

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.val:
            return True
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)

        return False

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node, a=0):
        if node is not None:
            self._print_tree(node.left, a + 1)
            print('.' * a, node.val, sep='')
            self._print_tree(node.right, a + 1)


with open('input.txt', 'r') as file:
    tree = Tree()
    for line in file:
        line = line.rstrip().split()
        if line[0] == 'ADD':
            num = int(line[1])
            tree.add(num)
        elif line[0] == 'SEARCH':
            num = int(line[1])
            if not tree.find(num):
                print('NO')
            else:
                print('YES')
        else:
            tree.print_tree()
