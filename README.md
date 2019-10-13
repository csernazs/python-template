# python-template
Cookiecutter template for my projects

It creates a directory structure for python development with a `Makefile` which most importantly creates a `.venv` directory which will have all the development requirements for the project. Run `make dev` to make it happen.

It also creates an entry point in setup.py so if you want to start with an executable script, then it will come very helpful (otherwise you can remove the setup.py lines and the empty script created).

## Usage

```
cookiecutter gh:csernazs/python-template
```
