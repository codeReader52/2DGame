from statemachine import State, StateMachine


class RaiderCharacterSM(StateMachine):
  idle = State(initial=True)
  run = State()
  jump = State()
  # attack = State()

  trigger_run = idle.to(run)
  stop_run = run.to(idle)
  trigger_jump = idle.to(jump) | run.to(jump)
  finish_jump = jump.to(idle)

  def __init__(self, on_enter_state, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.allow_event_without_transition = True
    self.on_enter_state = on_enter_state

  def on_enter_idle(self, event: str, source: State):
    if not hasattr(self, 'on_enter_state'):
      return

    self.on_enter_state["idle"](event, source)

  def on_enter_jump(self, event: str, source: State):
    if not hasattr(self, 'on_enter_state'):
      return

    self.on_enter_state["jump"](event, source)

  def on_enter_run(self):
    if not hasattr(self, 'on_enter_state'):
      return

    self.on_enter_state["run"]()


# class DirectionsM(StateMachine):
#   right = State(initial=True)
#   left = State()
