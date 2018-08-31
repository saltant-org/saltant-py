"""Contains the saltant API client."""

# TODO(mwiens91): add support for JWT auth tokens
# TODO(mwiens91): specify what happens when default timeout is exhausted

import os
import requests
from saltant.constants import DEFAULT_TIMEOUT_SECONDS
from saltant.exceptions import BadEnvironmentError


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

    Attributes:
        hostname (str): The URL of the saltant API.
    """
    def __init__(
            self,
            hostname,
            username=None,
            password=None,
            auth_token=None,
            default_timeout=DEFAULT_TIMEOUT_SECONDS):
        """Initialize the saltant API client.

        Args:
            hostname (str): The URL of the saltant API.
            username (str): The registered user's name.
            password (str): The registered user's password.
            auth_token (str): The registered user's authentication token.
            default_timeout (:obj:`int`, optional): The maximum number
                of seconds to wait for a request to complete. Defaults
                to 90 seconds.
        """
        # TODO(mwiens91): use the timeout
        self.hostname = hostname

    @classmethod
    def from_env(cls, default_timeout=DEFAULT_TIMEOUT_SECONDS):
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

        Args:
            default_timeout (:obj:`int`, optional): The maximum number
                of seconds to wait for a request to complete. Defaults to 90
                seconds.

        Returns:
            :class:`Client`: A saltant API client object.

        Raises:
            :class:`BadEnvironmentError`: The user has an incorrectly
                configured environment.
        """
        # Get variables from environment
        try:
            hostname = os.environ['SALTANT_HOSTNAME']
        except KeyError:
            raise BadEnvironmentError("SALTANT_HOSTNAME not defined!")

        try:
            # Try to get an auth token
            auth_token = os.environ['SALTANT_AUTH_TOKEN']

            # Return the configured client
            return cls(
                hostname=hostname,
                auth_token=auth_token,
                default_timeout=default_timeout,)
        except KeyError:
            pass

        # No auth token available. Try getting username and password.
        username = os.environ.get('SALTANT_USERNAME')
        password = os.environ.get('SALTANT_PASSWORD')

        if not username or not password:
            raise BadEnvironmentError("Authentication env vars not defined!")

        # Return the configured client
        return cls(
            hostname=hostname,
            username=username,
            password=password,
            default_timeout=default_timeout,)


# Allow convenient import access to environment-configured client
from_env = Client.from_env
