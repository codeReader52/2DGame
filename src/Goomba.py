import pygame


class Enemy:

  def __init__(self, position, radius, screen):
    self.position = position
    self.radius = radius
    self.screen = screen

  def draw(self):
    pygame.draw.circle(self.screen, (94, 50, 3), self.position, self.radius)
