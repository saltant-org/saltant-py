"""Classes for task queue model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from saltant.constants import (
    HTTP_201_CREATED,
)
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
    def __init__(self,
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


class TaskQueueManager(ModelManager):
    """Manager for task queues.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task instances.
        detail_url (str): The URL format to get specific task instances.
        model (:class:`TaskQueue`): The model of the task instance being
            used.
    """
    list_url = 'taskqueues/'
    detail_url = 'taskqueues/{id}/'
    model = TaskQueue

    def create(self,
               name,
               description="",
               private=False,
               active=True,):
        """Create a task queue.

        Args:
            name (str): The name of the task queue.
            description (str, optional): A description of the task queue.
            private (bool, optional): A boolean specifying whether the
                queue is exclusive to its creator. Defaults to False.
            active (bool, optional): A boolean specifying whether the
                queue is active. Default to True.

        Returns:
            :obj:`TaskQueue`: A task queue model instance representing
                the task queue just created.
        """
        # Create the object
        request_url = self._client.base_api_url + self.list_url
        data_to_post = {
            "name": name,
            "description": description,
            "private": private,
            "active": active,}

        response = self._client.session.post(request_url, data=data_to_post)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_201_CREATED,)

        # Return a model instance representing the task instance
        return self.response_data_to_model_instance(response.json())
