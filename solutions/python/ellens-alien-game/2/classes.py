"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health = max(0, self.health - 1)

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, alien):
        # To be defined later
        pass


def new_aliens_collection(coord_list: list[tuple[int]]) -> list[Alien]:
    """Create a list of Alien objects.
    
    params: coord_list: list[tuple[int]] - (x, y) coordinate pairs for each alien
    return: list: list[Alien] - A list of Alien objects
    """

    return [Alien(coords[0], coords[1]) for coords in coord_list]
