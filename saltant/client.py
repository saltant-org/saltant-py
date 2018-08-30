"""Contains the saltant API client."""

# TODO(mwiens91): add support for JWT auth tokens
# TODO(mwiens91): specify what happens when default timeout is exhausted

import os


class Client:
    """API client for communicating with a saltant server.

    For authentication you need to provide either a username and
    password, or an authentication token. If all three variables are
    provided, the authentication token is used and the username and
    password are ignored.

    Example:

        >>> import saltant
        >>> client = saltant.Client(
        ...     hostname='https://shahlabjobs.ca',
        ...     auth_token='p0gch4mp101fy451do9uod1s1x9i4a')

    Args:
        hostname (str): The URL of the saltant API.
        username (str): The registered user's name.
        password (str): The registered user's password.
        auth_token (str): The registered user's authentication token.
        default_timeout (int): The maximum number of seconds to wait for
            a request to complete. Defaults to 90 seconds.
    """
    def __init__(
            self,
            hostname,
            username=None,
            password=None,
            auth_token=None,
            default_timeout=90):
        """Initialize the saltant API client."""
        pass

    @classmethod
    def from_env(cls):
        """Return a client configured from environment variables.

        Essentially copying this:
        https://github.com/docker/docker-py/blob/master/docker/client.py#L43.

        The environment variables looked for are the following:

        .. envvar:: SALTANT_HOST

            The URL to the saltant host.

        .. envvar:: SALTANT_USERNAME

            The registered saltant user's name.

        .. envvar:: SALTANT_PASSWORD

            The registered saltant user's password.

        .. envvar:: SALTANT_AUTH_TOKEN

            The registered saltant user's authentication token.

        For authentication you need to provide either a username and
        password, or an authentication token. If all three variables are
        provided, the authentication token is used and the username and
        password are ignored.

        Example:

            >>> import saltant
            >>> client = saltant.from_env()
        """
        pass


# Allow convenient import access to environment-configured client
from_env = Client.from_env
