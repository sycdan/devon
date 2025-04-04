from devon.cli_client import CliClient


class Kustomize(CliClient):
  def __init__(self):
    super().__init__("kustomize")

  @property
  def is_installed(self):
    return self.call("version")
