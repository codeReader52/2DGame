import csv
import typing
from pygame import Surface
from StatefulSprite import StatefulSprite


class SpriteActor:

  def __init__(self, screen: Surface, asset_list: str, asset_folder: str):
    self.sprite_by_state: typing.Dict[str, StatefulSprite] = {}
    with open(asset_list, 'r') as state_file:
      for [sprite_file, _top, _left, state] in csv.reader(state_file, delimiter=' '):
        if state not in self.sprite_by_state:
          self.sprite_by_state[state] = StatefulSprite(screen, "Raider", 100)

        self.sprite_by_state[state].add_frame(asset_folder + sprite_file)

  def get_size(self, state: str):
    return self.sprite_by_state[state].get_size()

  def draw(self, state: str, lower_left: typing.Tuple[int, int], flip_vertically: bool):
    return self.sprite_by_state[state].draw(lower_left, flip_vertically)

  def update(self, state, dt: int):
    return self.sprite_by_state[state].update(dt)
