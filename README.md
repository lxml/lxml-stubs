# lxml-stubs

## About

This repository contains external type annotations (see
[PEP 484](https://www.python.org/dev/peps/pep-0484/)) for the
[lxml](http://lxml.de/) package. Such type annotations are normally included
in [typeshed](https://www.github.com/python/typeshed), but lxml's annotations were
frequently problematic and have therefore been deleted from typeshed. In particular, the stubs
are incomplete and it has been difficult to provide complete stubs.

This repo provides lxml stubs as they existed in typeshed for those who find them useful.
Eventually, it should become a PEP 561-style stubs package.

## Usage

To use these stubs with [mypy](https://github.com/python/mypy), you have to
install the `lxml-stubs` package.

If you want to use the stubs as-is, you can build and install the package
directly from its repository:

    $ pip install https://github.com/lxml/lxml-stubs.git

If you want to make local modifications, you can clone this repository and
tell `pip` to install a link to the cloned source tree:

    $ pip install -e /path/to/lxml-stubs

## Contributing

Contributions should follow the same style guidelines as
[typeshed](https://github.com/python/typeshed/blob/master/CONTRIBUTING.md).

## Git history

The early git history of this repo contains commits from typeshed, filtered to only changes that
affect typeshed (using `git filter-branch`).

## Authors

This repository was created by Jelle Zijlstra. Numerous others have contributed to the
lxml stubs; see the git history for details.

## TODOs

- Provide testing (both a local test script and a Travis setup)
- Provide a PEP 561-style setup script.
