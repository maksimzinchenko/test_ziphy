source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]


def to_tree(source):
    '''
    Converts tuple list to tree from dicts
    '''
    tree = {}
    for i in source[::-1]:
        element = {}
        if i[1] not in tree:
            element = {i[1]: {}}
        else:
            element = {i[1]: tree[i[1]]}
            tree.pop(i[1])
        if i[0] in tree:
            tree[i[0]].update(element)
        else:
            tree[i[0]] = element
    # remove None from tree root and sort tree dict
    tree = dict(sorted(tree[None].items()))
    return tree


expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
