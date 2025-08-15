import pygame


class HealthBar:

  def __init__(self, width, height, screen):
    self.health = 100
    self.width = width
    self.height = height
    self.screen = screen

  def draw(self):
    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(400, 10, self.width, self.height))
    pygame.draw.rect(self.screen, (
        0,
        255,
        0,
    ), pygame.Rect(400, 10, self.width * self.health / 100, self.height))
