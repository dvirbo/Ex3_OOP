from position import Position


class Node(object):
    """
    this class represent a node that contain:
     * uniq key
     * 3D position
     * tag - to know if we visit or not (0/1)
     * weight - to use in algo
     * inEdges - dict that will contain the edged that this node is the src of them
     * outEdges - dict that will contain the edged that this node is the dest of them
    """

    def __init__(self, key: int, pos: tuple):
        """
        :param key: uniq key of the node
        :param pos: geo position
        """
        self.key = key
        self.tag = 0
        self.weight = None
        self.inEdges = {}
        self.outEdges = {}
        if pos is not None:
            self.pos = Position(pos)
        else:
            self.pos = pos

    def setTag(self, tag):
        self.tag = tag

    def __str__(self) -> str:
        return f"id: {self.id}, pos: {self.pos}"

    def __repr__(self) -> str:
        return f"id: {self.id}, pos: {self.pos}"


