from pygame import Surface, draw
from pymunk import Space, Vec2d
from PhysicsComponent import PhysicsComponent


class Enemy:

  def __init__(self, space: Space, mass: float, init_position: Vec2d, radius: float, elasticity: float, screen: Surface):
    self.physics = PhysicsComponent(space,
                                    mass, (init_position[0], screen.get_height() - init_position[1]), {"default": (radius, radius)},
                                    "default",
                                    elasticity=elasticity)
    self.radius = radius
    self.screen = screen

  def draw(self):
    bb = self.physics.get_bounding_box()
    draw.circle(self.screen, (94, 50, 3), ((bb.left + bb.right) / 2.0, self.screen.get_height() - (bb.bottom + bb.top) / 2.0), self.radius)
