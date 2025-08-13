from pymunk import Vec2d


class Config:
  gravity = Vec2d(0, -900)
  attack_duration_ms = 1000
  ground_height = 150
  raider_mass = 1
  raider_initial_position = Vec2d(300, 250)
  raider_vertical_jump = Vec2d(0, 35000)
  raider_diagonal_right_jump = Vec2d(5000, 35000)
  raider_diagonal_left_jump = Vec2d(-5000, 35000)
  raider_run_right_velocity = Vec2d(130, 0)
  raider_run_left_velocity = Vec2d(-130, 0)
