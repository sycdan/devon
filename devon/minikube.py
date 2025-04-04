from devon.cli_client import CliClient


class Minikube(CliClient):
  def __init__(self):
    super().__init__("minikube")

  @property
  def is_installed(self):
    return self.call("version")

  @property
  def is_initialized(self):
    return self.call("status")

  def delete(self):
    return self.call("delete")

  def start(self):
    return self.call("start")
