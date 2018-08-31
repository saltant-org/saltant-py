"""Contains exceptions used throughout the program."""


class AuthenticationError(Exception):
    """The authentication provided was invalid."""
    pass


class BadEnvironmentError(Exception):
    """The user has an improperly configured environment."""
    pass
