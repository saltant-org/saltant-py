"""Classes for task queue model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from saltant.constants import (
    HTTP_200_OK,
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
        manager (:class:`saltant.models.task_queue.TaskQueueManager`):
            The task queue manager which spawned this task queue. This
            is used to add a put method to the task queue instance.
    """
    def __init__(self,
                 id,
                 user,
                 name,
                 description,
                 private,
                 active,
                 manager,):
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
            manager (:class:`saltant.models.task_queue.TaskQueueManager`):
                The task queue manager which spawned this task instance.
                This is used to add a put method to the task queue
                instance.
        """
        self.id = id
        self.user = user
        self.name = name
        self.description = description
        self.private = private
        self.active = active
        self.manager = manager

    def __str__(self):
        """String representation of the task queue."""
        return self.name

    def put(self):
        """Updates this task queue on the saltant server.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just updated.
        """
        return self.manager.put(self)


class TaskQueueManager(ModelManager):
    """Manager for task queues.

    Attributes:
        _client (:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task queues.
        detail_url (str): The URL format to get specific task queues.
        model (:class:`saltant.models.task_queue.TaskQueue`): The model
            of the task queue being used.
    """
    list_url = 'taskqueues/'
    detail_url = 'taskqueues/{id}/'
    model = TaskQueue

    def get(self, id=None, name=None):
        """Get a task queue.

        Either the id xor the name of the task type must be specified.

        Args:
            id (int, optional): The id of the task type to get.
            name (str, optional): The name of the task type to get.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                requested.

        Raises:
            ValueError: Neither id nor name were set *or* both id and
                name were set.
        """
        # Validate arguments - use an xor
        if not ((id is None) ^ (name is None)):
            raise ValueError(
                "Either id or name must be set (but not both!)")

        # If it's just ID provided, call the parent function
        if id is not None:
            return super(TaskQueueManager, self).get(id=id)

        # Try getting the task queue by name
        return self.list(filters={"name": name})[0]

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
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just created.
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

    def put(self, task_queue):
        """Updates a task queue on the saltant server.

        Args:
            task_queue (:class:`saltant.models.task_queue.TaskQueue`):
                A task queue model instance to be used for updating the
                corresponding model instance on the saltant server.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just updated.
        """
        # Update the object
        request_url = (
            self._client.base_api_url
            + self.detail_url.format(id=task_queue.id))
        data_to_put = {
            "name": task_queue.name,
            "description": task_queue.description,
            "private": task_queue.private,
            "active": task_queue.active,}

        response = self._client.session.put(request_url, data=data_to_put)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_200_OK,)

        # Return a model instance representing the task instance
        return self.response_data_to_model_instance(response.json())

    def response_data_to_model_instance(self, response_data):
        """Convert response data to a task queue model.

        Args:
            response_data (dict): The data from the request's response.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queuemodel instance representing the task queue
                from the reponse data.
        """
        # Add in this manager to the data
        response_data['manager'] = self

        # Instantiate a model for the task queue
        return super(
            TaskQueueManager,
            self).response_data_to_model_instance(response_data)
