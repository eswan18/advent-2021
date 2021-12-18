from copy import deepcopy
from dataclasses import dataclass

from .node import Node, LeafNode


@dataclass
class BranchNode(Node):
    left: Node
    right: Node

    def __add__(self, other: 'BranchNode') -> 'BranchNode':
        left = self.from_line(str(self))
        right = self.from_line(str(other))
        new = self.__class__(parent=None, left=left, right=right)
        new.fully_reduce()
        return new

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

    def reduce(self) -> bool:
        '''Reduce. Returns True if a reduction was found.'''
        # Explode the first 4-deep pair.
        for n in self.dfs():
            if n.depth == 4 and not n.is_leaf():
                n.explode()
                return True
        for n in self.dfs():
            if n.is_leaf() and n.value >= 10:
                n.split()
                return True
        return False

    def fully_reduce(self) -> None:
        reducible = True
        while reducible:
            reducible = self.reduce()

    def __str__(self) -> str:
        return f'[{str(self.left)},{str(self.right)}]'

    @classmethod
    def from_line(cls, line: str) -> 'BranchNode':
        assert line[0] == '['
        assert line[-1] == ']'
        line = line[1:-1]
        bracket_count = 0
        for i, c in enumerate(line):
            if c == '[':
                bracket_count += 1
            elif c == ']':
                bracket_count -= 1
            elif c == ',' and bracket_count == 0:
                left = line[:i]
                right = line[i+1:]
                if '[' in left:
                    left = cls.from_line(left)
                else:
                    left = LeafNode(parent=None, value=int(left))
                if '[' in right:
                    right = cls.from_line(right)
                else:
                    right = LeafNode(parent=None, value=int(right))
                node = BranchNode(parent=None, left=left, right=right)
                node.left.parent = node
                node.right.parent = node
                return node
