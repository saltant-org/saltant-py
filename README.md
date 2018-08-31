[![Build Status](https://travis-ci.com/mwiens91/saltant-py.svg?branch=master)](https://travis-ci.com/mwiens91/saltant-py)
[![Documentation Status](https://readthedocs.org/projects/saltant-py/badge/?version=latest)](https://saltant-py.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/saltant-py.svg)](https://pypi.org/project/saltant-py/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/saltant-py.svg)](https://pypi.org/project/saltant-py/)

# saltant SDK for Python

### NOTE: this project is an active work in progress

This attempts to follow the coding paradigms of
[docker-py](https://github.com/docker/docker-py) fairly closely.

## Sketch !

```python
"""Sketch code for development.

To be updated whenever I don't have a clear way forward (provided spare
time, etc).
"""
from saltant.main import Client

SALTANT_API_URL = "https://asdlkfajklfs.com/api"
SALTANT_AUTH_TOKEN = "1j2h3iou13h" # or could use USERNAME and PASSWORD

# Connect to the saltant server
my_saltant = Client(
    url=SALTANT_API_URL,
    auth_token=SALTANT_AUTH_TOKEN,)

# My stuff
my_saltant.user.task_types
my_saltant.user.id

# Create an instance
my_saltant.task_types.list(
    iregex="asdf",)
```
