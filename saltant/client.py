"""Contains the saltant API client."""

class Client:
    """API client for saltant."""
    @classmethod
    def from_env(cls):
        """Return a client configured from environment variables.

        Essentially copying this:
        https://github.com/docker/docker-py/blob/master/docker/client.py#L43
        """

# Allow conventient import access to environment-configured client
from_env = Client.from_env
