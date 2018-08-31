"""Import saltant client for convenient access."""

# The try block is so that setup.py can peek into the directory without
# having external packages installed.
try:
    from .client import Client, from_env
except ImportError:
    pass
