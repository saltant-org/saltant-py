"""Classes for user model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from .resource import Model, ModelManager


class User(Model):
    """Base model for a user.

    Attributes:
        username (str): The user's username.
        email (str): The user's email.
    """
    def __init__(self, username, email):
        """Initialize a user.

        Args:
            username (str): The user's username.
            email (str): The user's email.
        """
        self.username = username
        self.email = email

    def __str__(self):
        """String representation of the user."""
        return self.username


class UserManager(ModelManager):
    """Manager for task queues.

    Attributes:
        _client (:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task queues.
        detail_url (str): The URL format to get specific task queues.
        model (:class:`saltant.models.user.User`): The model of the task
            queue being used.
    """
    list_url = 'users/'
    detail_url = 'users/{id}/'
    model = User

    def get(self, username):
        """Get a user.

        Args:
            name (str): The username of the user to get.

        Returns:
            :class:`saltant.models.user.User`:
                A user model instance representing the user requested.
        """
        # Call the parent function
        return super(UserManager, self).get(id=username)
