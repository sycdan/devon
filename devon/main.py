#!/usr/bin/env python
import typer
from castaway import config
from pynput import keyboard
from rich.console import Console
from rich.live import Live
from rich.table import Table

from devon import APP_VERSION
from devon.minikube import Minikube

app = typer.Typer()
console = Console()
minikube = Minikube()
noisy = False


def begin(message):
  return console.status(message + "... ")


def fail(message="fail"):
  """Exit with an error code after printing the message."""
  typer.secho(message, fg=typer.colors.RED)
  raise typer.Exit(1)


def ok(message="ok"):
  """Print a success message with a check mark."""
  typer.secho(message, fg=typer.colors.GREEN)


def say(message):
  typer.echo(message)


class ClusterManager:
  def __init__(
    self,
    items,
  ):
    self.items = items
    self.selected_index = 0
    self.running = True

  def render_table(
    self,
  ):
    table = Table(
      show_header=True,
      header_style="bold magenta",
    )
    table.add_column(
      "Index",
      justify="center",
    )
    table.add_column(
      "Item",
      justify="left",
    )

    for (
      i,
      item,
    ) in enumerate(self.items):
      if i == self.selected_index:
        table.add_row(
          f"[bold yellow]{i}[/bold yellow]",
          f"[bold green]{item}[/bold green]",
        )
      else:
        table.add_row(
          f"{i}",
          item,
        )

    return table

  def on_key_press(
    self,
    key,
  ):
    try:
      if key == keyboard.Key.up:
        self.selected_index = (self.selected_index - 1) % len(self.items)
      elif key == keyboard.Key.down:
        self.selected_index = (self.selected_index + 1) % len(self.items)
      elif key == keyboard.Key.esc:
        self.running = False
    except Exception as e:
      console.print(f"[red]Error: {e}[/red]")

  def run(
    self,
  ):
    with Live(
      self.render_table(),
      refresh_per_second=10,
      console=console,
    ) as live:
      with keyboard.Listener(on_press=self.on_key_press) as listener:
        while self.running:
          live.update(self.render_table())
        listener.stop()


@app.command()
def version():
  """Show the application version number."""
  print(APP_VERSION)


@app.command()
def mk(
  kustomize_root=config("DEVON_KUSTOMIZE_ROOT", default="./k8s/"),
  rebuild: bool = False,
):
  """Manage the local Kubernetes (Minikube) cluster."""
  if noisy:
    say(f"{kustomize_root=}")

  if not minikube.is_installed:
    fail("minikube is not installed")

  if rebuild:
    with begin("deleting cluster"):
      if minikube.delete():
        ok()
      else:
        fail()

  if not minikube.is_initialized:
    with begin("creating cluster"):
      if minikube.start():
        ok()
      else:
        fail()

  items = [
    f"Item {i}"
    for i in range(
      1,
      21,
    )
  ]
  app = ClusterManager(items)
  app.run()


@app.callback()
def main(
  verbose: bool = typer.Option(
    False,
    "--verbose",
    "-v",
    help="Enable verbose output.",
  ),
):
  global noisy
  noisy = verbose


# enable running via python -m devon.main
if __name__ == "__main__":
  app()
