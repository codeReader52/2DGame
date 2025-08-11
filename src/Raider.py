import typing
from pygame import Surface
from pymunk import Space, Body, Poly
import csv
import typing

from CharacterStateMachine import RaiderCharacterSM
from StatefulSprite import StatefulSprite


class Raider:

  def __init__(self, screen: Surface, space: Space):
    self.rect = None
    self.sm = RaiderCharacterSM()
    self.sprite_by_state: typing.Dict[str, StatefulSprite] = {}

    with open("./assets/Raider_1_spritelist.psd.txt", 'r') as state_file:
      for [sprite_file, _top, _left, state] in csv.reader(state_file, delimiter=' '):
        if state not in self.sprite_by_state:
          self.sprite_by_state[state] = StatefulSprite(screen, "Raider", 150)

        self.sprite_by_state[state].add_frame("./assets/Raider_1/" + sprite_file)

    self.body = Body(mass=50)
    self.body.position = (300, 300)
    self.shapes = {
        "idle": Poly.create_box(self.body, self.sprite_by_state["idle"].get_size()),
        "run": Poly.create_box(self.body, self.sprite_by_state["run"].get_size()),
        "jump": Poly.create_box(self.body, self.sprite_by_state["jump"].get_size())
    }
    self.space = space
    self.space.add(self.body, self.shapes["idle"])
    self.screen_height = screen.get_height()

  def get_sprite(self):
    return self.sprite_by_state[self.sm.current_state.name.lower()]

  def update(self, dt: float):
    self.get_sprite().update(dt)

  def draw(self):
    bb = self.shapes["idle"].cache_bb()
    self.get_sprite().draw((bb.left, self.screen_height - bb.bottom))

  def run_right(self):
    if self.sm.current_state == RaiderCharacterSM.idle:
      self.body.velocity = (20, 0)
    self.sm.trigger_run()

  def run_left(self):
    self.sm.trigger_run()

  def stop_run(self):
    self.sm.stop_run()

  def jump(self):
    if self.sm.current_state == RaiderCharacterSM.run:
      self.body.apply_force_at_local_point((5000, -5000))
    elif self.sm.current_state == RaiderCharacterSM.idle:
      self.body.apply_force_at_local_point((0, -5000))
    self.sm.trigger_jump()

  def finish_jump(self):
    self.sm.finish_jump()

  def get_jump_duration(self):
    return 1200
