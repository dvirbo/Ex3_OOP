class Node:

    id = None
    pos = None
    tag = None
    weight = None

    def __init__(self, id_num: int, position: tuple):
        self.id = id_num
        self.pos = position
        self.weight = None
        self.tag = 0

    def __str__(self) -> str:
        return f"id: {self.id}, pos: {self.pos}"

    def __repr__(self) -> str:
        return f"id: {self.id}, pos: {self.pos}"
