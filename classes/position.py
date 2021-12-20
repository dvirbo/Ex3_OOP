import math


class Position(object):
    """
    this class represent a position point in 3D dimension
    """

    def __init__(self, pos: tuple = None):
        """
        :param pos: constructor that get tuple of 3 parameters: x, y, z
        """
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

    def __eq__(self, other):
        if other is None:
            return 1
        if not isinstance(other, Position):
            return 1
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return 0
        else:
            return 1

    def distance(self, dest):
        """
        :param dest: pos of the dist point
        :return: the distance between the two point
        """
        return math.sqrt(math.pow(self.x - dest.x, 2) + math.pow(self.y - dest.y) + math.pow(self.z - dest.z, 2))



