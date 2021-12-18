from functools import cached_property
from typing import Optional, Iterator
from dataclasses import dataclass, field


@dataclass
class Node:
    parent: Optional['Node'] = field(repr=False)

    def is_root(self) -> bool:
        return parent is not None

    def is_leaf(self) -> bool:
        return not hasattr(self, 'children')

    @property
    def parents(self) -> Iterator['BranchNode']:
        n = self
        while n.parent:
            yield n.parent
            n = n.parent

    @cached_property
    def depth(self) -> int:
        if self.parent:
            return self.parent.depth + 1
        else:
            return 0

    def bfs(self) -> Iterator['Node']:
        raise NotImplementedError

    def dfs(self) -> Iterator['Node']:
        '''Depth-first search, left to right.'''
        if self.is_leaf():
            yield self
        else:
            yield self
            yield from self.left.dfs()
            yield from self.right.dfs()


@dataclass
class LeafNode(Node):
    value: int

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}({self.value})'

@dataclass
class BranchNode(Node):
    left: Node
    right: Node

    def __add__(self, other: 'BranchNode') -> 'BranchNode':
        left = deepcopy(self)
        right = deepcopy(other)
        return self.__class__(left, right)

    @property
    def children(self) -> tuple[Node, Node]:
        return (self.left, self.right)
