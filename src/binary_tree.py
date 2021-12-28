from __future__ import annotations
from typing import Type, TypeVar


Tree = TypeVar('T', bound='Tree')

class Tree:
    def __init__(self : type(Tree) ,right : type(Tree)=None ,left : type(Tree)=None ) -> None:
        self.right = right 
        self.left = left 

    @classmethod
    def length(cls , root : Tree) -> int:
        return 3