from devon.utils import run_ok


class CliClient:
  def __init__(self, exe: str):
    self.exe = exe

  def call(self, command, *args):
    return run_ok(self.exe, command, *args)
