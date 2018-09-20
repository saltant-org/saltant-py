"""Classes for task queue model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from .resource import Model, ModelManager


class TaskQueue(Model):
    """Base model for a task queue.

    Attributes:
        id (int): The ID of the task queue.
        user (str): The user who created the task queue.
        name (str): The name of the task queue.
        description (str): The description of the task queue.
        private (bool): A Booleon signalling whether the queue can only
            be used by its associated user.
        active (bool): A Booleon signalling whether the queue is active.
    """
    def __init__(
            self,
            id,
            user,
            name,
            description,
            private,
            active,):
        """Initialize a task queue.

        Args:
            id (int): The ID of the task queue.
            user (str): The user who created the task queue.
            name (str): The name of the task queue.
            description (str): The description of the task queue.
            private (bool): A Booleon signalling whether the queue can
                only be used by its associated user.
            active (bool): A Booleon signalling whether the queue is
                active.
        """
        self.id = id
        self.user = user
        self.name = name
        self.description = description
        self.private = private
        self.active = active

    def __str__(self):
        """String representation of the task queue."""
        return self.name
