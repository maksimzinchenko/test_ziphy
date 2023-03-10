# test_ziphy

```
Test Python

Write a function that builds a tree based on a list of tuples of id (parent id, offspring id),
where None is the id of the root node.

How this should work:

Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
где None - id корневого узла.
Пример работы:

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

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
```
====================


Solution:
In the first pass, we create a dict with plane child nodes.
In the second pass, we create root nodes of tree, if the parent is specified as None or rebind - we generate a chain-branch of nodes from the nodes dict.
At the output, the created node tree chains from the nodes dict will be attached to the root of tree dict.
