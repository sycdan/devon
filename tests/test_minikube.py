from devon.minikube import Minikube


def test_is_installed_yes(mocker):
  mocker.patch("devon.minikube.run_ok", lambda *_, **__: True)
  minikube = Minikube()
  assert minikube.is_installed


def test_is_installed_no(mocker):
  mocker.patch("devon.minikube.run_ok", lambda *_, **__: False)
  minikube = Minikube()
  assert not minikube.is_installed
