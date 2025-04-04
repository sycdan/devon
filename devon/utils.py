import subprocess


def run_ok(*args):
  """Synchronously run a command on the host."""
  result = subprocess.run(args, capture_output=True, text=True)
  if result.returncode == 0:
    return True
  else:
    return False
