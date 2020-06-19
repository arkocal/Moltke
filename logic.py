
class GameObject:
    def __init__(self, position, box):
        self.position = position
        self.box = box

    @property
    def top_left(self):
        return self.position - (0.5 * self.box)

    @property
    def bottom_right(self):
        return self.position + (0.5 * self.box)

    def is_colliding(self, other):
        me_tl = self.top_left
        me_br = self.bottom_right
        he_tl = other.top_left
        he_br = other.bottom_right
        
        if(me_tl.x < he_tl.x)
            return False
        if(me_br.x > he_tl.x)
            return False
        if(me_tl.y < he_tl.y)
            return False
        if(me_br.y > he_tl.y)
            return False
    
class Player(GameObject):
    def __init__(self, position, movement):
        self.movement = movement

    def turn_cw(self):
        self.movement.rotate(90)

    def turn_ccw(self):
        self.movement.rotate(-90)

class Obstacle(GameObject):
    pass

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def tick(self):
        for p in self.players:
            p.position += p.movement

    def turn_cw()
        for p in self.players:
            p.turn_cw()

    def turn_ccw()
        for p in self.players:
            p.turn_cw()
        
