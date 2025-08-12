from pymunk import Body, Poly, Space, moment_for_box
import typing

from GameConfig import Config


class RaiderPhysicsBody:
  COLLISION_TYPE = 2

  def __init__(self, space: Space, body_size_by_state: typing.Dict[str, typing.Tuple[float, float]], initial_state):
    self.body = Body(mass=Config.raider_mass)
    self.body.position = Config.raider_initial_position

    self.shapes: typing.Dict[str, Poly] = {}
    for state, body_size in body_size_by_state.items():
      self.shapes[state] = Poly.create_box(self.body, body_size)
      self.shapes[state].collision_type = self.COLLISION_TYPE

    self.space = space
    self.body.moment = moment_for_box(self.body.mass, body_size_by_state[initial_state])
    self.space.add(self.body, self.shapes[initial_state])
    self.current_state = initial_state

  def apply_force(self, force: typing.Tuple[float, float]):
    self.body.apply_force_at_local_point(force)

  def set_velocity(self, velocity: typing.Tuple[float, float]):
    self.body.velocity = velocity

  def get_bounding_box(self):
    return self.shapes[self.current_state].cache_bb()

  def replace_shape(self, state: str):
    self.space.remove(self.shapes[self.current_state])
    self.current_state = state
    self.space.add(self.shapes[state])
