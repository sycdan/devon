# devon

Local cluster management, and other tools to aid development.

## Usage

```sh
pip install devon-cli

dev --help
```

## Configuration

devon will look for a `.env` file in the working directory.

These are the defaults, and how to override them:

```sh
export DEVON_KUSTOMIZE_ROOT=./k8s/
export DEVON_KUSTOMIZE_OVERLAY=local
```

## Caveats

devon only works with `minikube` and `kustomize` at this time.
