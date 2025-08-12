import pymunk
from pygame import Surface, draw, Rect

from GameConfig import Config

DARK_GREEN = (35, 48, 11)


class Ground:
  COLLISION_TYPE = 1

  def __init__(self, screen: Surface, space: pymunk.Space):
    self.screen = screen
    ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground_body.position = (screen.get_width() / 2, Config.ground_height / 2)
    shape = pymunk.Poly.create_box(ground_body, (screen.get_width(), Config.ground_height))
    shape.collision_type = self.COLLISION_TYPE
    space.add(ground_body, shape)

  def draw(self):
    draw.rect(
        self.screen,
        DARK_GREEN,
        Rect(0,
             self.screen.get_height() - Config.ground_height, self.screen.get_width(), Config.ground_height),
    )
