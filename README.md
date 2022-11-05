# Parcial 2 ATI

# Setup development environment

## Install system dependencies
These system dependencies are required, **Linux OS** is preferred.

1. bash
2. docker
3. docker-compose

## Setup

If you are using Linux, put this into your bashrc `.bashrc` OR `.zhsrc`, it's needed for the file permissions.

```bash
export UID=$(id -u)
export GID=$(id -g)
```

Run this command, to setup the development environment

```bash
bash ./shscripts/setup_dev.sh
```
Activate the server, to test if everything has worked

```bash
runserver
```

Visit `http://127.0.0.1:8000`
