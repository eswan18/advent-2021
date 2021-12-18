from copy import deepcopy
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

    def is_right(self) -> bool:
        if self.is_root():
            return False
        return self == self.parent.right

    def is_left(self) -> bool:
        if self.is_root():
            return False
        return self == self.parent.left

    def next_left_leaf(self) -> Optional['LeafNode']:
        current = self
        # Navigate up the tree until finding a place to go left.
        while not current.is_right():
            current = current.parent
            if current.is_root():
                return None
        # Switch to the left branch.
        current = current.parent.left
        # Go as deep to the right as possible within this branch.
        while not current.is_leaf():
            current = current.right
        return current

    def next_right_leaf(self) -> Optional['LeafNode']:
        current = self
        # Navigate up the tree until finding a place to go right.
        while not current.is_left():
            current = current.parent
            if current.is_root():
                return None
        # Switch to the right branch.
        current = current.parent.right
        # Go as deep to the left as possible within this branch.
        while not current.is_leaf():
            current = current.left
        return current


@dataclass
class LeafNode(Node):
    value: int

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}({self.value})'

    def __str__(self) -> str:
        return str(self.value)

@dataclass
class BranchNode(Node):
    left: Node
    right: Node

    def __add__(self, other: 'BranchNode') -> 'BranchNode':
        left = deepcopy(self)
        right = deepcopy(other)
        return self.__class__(parent=None, left=left, right=right)

    @property
    def children(self) -> tuple[Node, Node]:
        return (self.left, self.right)

    def explode(self) -> None:
        if self.is_root():
            raise TypeError
        if not self.left.is_leaf() or not self.right.is_leaf():
            raise TypeError
        # Add the values to the next left- and right-most leaves.
        left_v = self.left.value
        right_v = self.right.value
        next_left_leaf = self.next_left_leaf()
        if next_left_leaf:
            next_left_leaf.value += left_v
        next_right_leaf = self.next_right_leaf()
        if next_right_leaf:
            next_right_leaf.value += right_v
        # Replace this node with a leaf node of value 0.
        zero = LeafNode(parent=self.parent, value=0)
        if self.is_left():
            self.parent.left = zero
        else:
            self.parent.right = zero


    def __str__(self) -> str:
        return f'[{str(self.left)},{str(self.right)}]'
