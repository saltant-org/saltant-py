![Python version](https://img.shields.io/badge/python-3-blue.svg)

# saltant SDK for Python

### NOTE: this project is an active work in progress

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
