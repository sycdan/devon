from pathlib import Path

import typer
from castaway import config

from devexy.constants import APP_NAME

APP_DIR = Path(typer.get_app_dir(APP_NAME))
APP_DIR.mkdir(parents=True, exist_ok=True)

DEBUG: bool = config("DEVEXY_DEBUG", default=False, cast=bool)

KUSTOMIZE_ROOT: Path = config("DEVEXY_KUSTOMIZE_ROOT", default="./k8s/", cast=Path)
KUSTOMIZE_OVERLAY: str = config("DEVEXY_KUSTOMIZE_OVERLAY", default="local")
KUSTOMIZE_OVERLAY_DIR = KUSTOMIZE_ROOT / "overlays" / KUSTOMIZE_OVERLAY
LOCAL_PORT_ANNOTATION: str = config(
  "DEVEXY_LOCAL_PORT_ANNOTATION", default="devexy/local-port"
)
