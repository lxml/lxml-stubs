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

To use these stubs, clone this repo and point your type checker to it. For example, to use them in
[mypy](http://github.com/python/mypy), you can set the `$MYPYPATH` environment variable or set
`mypy_path = /path/to/lxml-stubs` in your `mypy.ini`.

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
