#!/usr/bin/env bash

python3 -m pip install --prefix=${HOME}/.local/ -e .[dev]
export PATH="${HOME}/.local/bin:${PATH}"
sphinx-build -b html docs pages
