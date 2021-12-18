from copy import deepcopy
from functools import cached_property
from typing import Optional, Iterator, TYPE_CHECKING
from dataclasses import dataclass, field


if TYPE_CHECKING:
    from branch_node import BranchNode


@dataclass
class Node:
    parent: Optional['Node'] = field(repr=False)

    def is_root(self) -> bool:
        return self.parent is None

    def is_leaf(self) -> bool:
        return not hasattr(self, 'children')

    @property
    def parents(self) -> Iterator['BranchNode']:
        n = self
        while n.parent:
            yield n.parent
            n = n.parent

    @property
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
        return self is self.parent.right

    def is_left(self) -> bool:
        if self.is_root():
            return False
        return self is self.parent.left

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

    def split(self) -> None:
        from .branch_node import BranchNode
        if self.value % 2: # odd
            left_v = self.value // 2
            right_v = (self.value // 2) + 1
        else: # even
            left_v = self.value // 2
            right_v = self.value // 2
        left = LeafNode(parent=None, value=left_v)
        right = LeafNode(parent=None, value=right_v)
        new_branch = BranchNode(parent=self.parent, left=left, right=right)
        left.parent = new_branch
        right.parent = new_branch
        # Replace this node with the new branch
        if self.is_left():
            self.parent.left = new_branch
        else:
            self.parent.right = new_branch
