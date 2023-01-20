import random

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


def to_tree2(source):
    '''
    List of tuples of refs to tree
    '''
    nodes = {ref_id: {} for _, ref_id in source}
    tree = {}
    for parent, child in source:
        if parent is None:
            tree[child] = nodes[child]
        else:
            nodes[parent][child] = nodes[child]
    return tree

def to_tree(source):
    '''
    List of tuples of refs to tree
    '''
    nodes = {}
    tree = {}
    
    for parent, child in source:
        nodes[child] = nodes.get(child, {})
        if parent is None:
            tree[child] = nodes.get(child, {})
        else:
            nodes[parent] = nodes.get(parent, {})
            nodes[parent][child] = nodes.get(child, {})

    return tree


expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
