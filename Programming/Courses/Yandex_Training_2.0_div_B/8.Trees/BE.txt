n = int(input())


def mke_tree(seq):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    node = tree
    for sym in seq:
        if sym == 'D':
            new = {'left': None, 'right': None, 'up': node, 'type': 'left'}
            node['left'] = new
            node = new
        elif sym == 'U':
            while node['type'] == 'right':
                node = node['up']
            node = node['up']
            new = {'left': None, 'right': None, 'up': node, 'type': 'right'}
            node['right'] = new
            node = new
    return tree


def traverse(root, prefix):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')
    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans


for _ in range(n):
    se = input()
    answer = traverse(mke_tree(se), [])
    print(len(answer))
    print(*answer, sep='\n')
