# Projeto de Viagens

## Getting Started

### Technologies

* [Python](https://www.python.org/) - 3.12.0
* [CLIPS](https://clipsrules.net/) to create rules
* [Git](https://git-scm.com/)
* [UV](https://docs.astral.sh/uv/) to manage dependencies


### Installation

This project needs UV installed at your machine. After you installed it, the first step is to clone this repository:

HTTPS:

```
git clone https://github.com/Avengers042/travel-backend.git
```

Or SSH:

```
git clone git@github.com:Avengers042/travel-backend.git
```

After you cloned this repository, you will need to install dependencies:

```
uv sync
```

Now there is a difference between other languages. In other ecossystems like Rust and NodeJS, you just install and the environment is managed by your CLI, e.g, npm and cargo.

In Python, every library is installed in a virtual environment (venv to be simple) and it is usually found at directory .venv at root of your project (poetry do this different from others CLI like uv and pip).

And to use this dependencies, you need to start the shell. Before tools like Poetry and UV exists, we install venv and do python -m venv .env (or .venv), but happily this is not needed anymore because this is automatically created).

To enter the venv:

```
source .venv/bin/activate
```

And to exit from this env at terminal (if you use VSCode you need to create another venv and choose to use this new venv or close the editor):

```
deactivate
```

And finally, to run the project:
```
uv run travel-backend/__init__.py
```
