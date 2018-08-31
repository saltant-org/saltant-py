"""Contains base classes for models and related classes."""


class Model(object):
    """Base class for representing a model.

    Attributes:
        client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
    """
    def __init__(self, _client):
        """Save the client so we can make API calls in the model.

        Args:
            _client (:py:class:`saltant.client.Client`): An
                authenticated saltant client.
        """
        self._client = _client

    def refresh(self):
        """Refresh the model with new API data."""
        raise NotImplementedError

    def __str__(self):
        """String representation of model."""
        raise NotImplementedError
