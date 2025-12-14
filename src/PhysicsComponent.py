from pymunk import Body, Poly, Space, moment_for_box, Vec2d
import typing


class PhysicsComponent:

  def __init__(self, space: Space, mass: float, position: Vec2d, body_size_by_state: typing.Dict[str, typing.Tuple[float, float]], initial_state,
               **shape_kwargs):
    self.body = Body(mass=mass)
    self.body.position = position
    self.shapes: typing.Dict[str, Poly] = {}
    for state, body_size in body_size_by_state.items():
      self.shapes[state] = Poly.create_box(self.body, body_size)
      self.shapes[state].collision_type = shape_kwargs.pop("collision_type", 0)
      self.shapes[state].elasticity = shape_kwargs.pop("elasticity", 0)

    self.space = space
    self.body.moment = moment_for_box(self.body.mass, body_size_by_state[initial_state])
    self.space.add(self.body, self.shapes[initial_state])
    self.current_state = initial_state

  def apply_force(self, force: Vec2d):
    self.body.apply_force_at_local_point(force)

  def set_velocity(self, velocity: Vec2d):
    self.body.velocity = velocity

  def get_bounding_box(self):
    return self.shapes[self.current_state].cache_bb()

  def replace_shape(self, state: str):
    self.space.remove(self.shapes[self.current_state])
    self.current_state = state
    self.space.add(self.shapes[state])

  def clear(self):
    # Clear linear velocity (set to (0, 0) vector)
    self.body.velocity = Vec2d(0, 0)

    # Clear angular velocity (set to 0 scalar)
    self.body.angular_velocity = 0

    # Clear applied force (set to (0, 0) vector)
    self.body.force = Vec2d(0, 0)

    # Clear applied torque (set to 0 scalar)
    self.body.torque = 0
