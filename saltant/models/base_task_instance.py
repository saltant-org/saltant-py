"""Base class for task instance models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from .resource import Model


class BaseTaskInstance(Model):
    """Base class for a task instance.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        name (str): The name of the task instance.
        uuid (str): The UUID of the task instance.
        state (str): The state of the task instance.
        user (str): The username of the user who started the task.
        task_queue (int): The ID of the task queue the instance is
            running on.
        task_type (int): The ID of the task type for the instance.
        datetime_created (:class:`datetime.datetime`): The datetime when
            the task instance was created.
        datetime_finished (:class:`datetime.datetime`): The datetime
            when the task instance finished.
        arguments (dict): The arguments the task instance was run with.
    """
    def __init__(
            self,
            _client,
            name,
            uuid,
            user,
            task_queue,
            task_type,
            datetime_created,
            datetime_finished,
            arguments,):
        """Initialize a task instance.

        Args:
            _client (:py:class:`saltant.client.Client`): An
                authenticated saltant client.
            name (str): The name of the task instance.
            uuid (str): The UUID of the task instance.
            state (str): The state of the task instance.
            user (str): The username of the user who started the task.
            task_queue (int): The ID of the task queue the instance is
                running on.
            task_type (int): The ID of the task type for the instance.
            datetime_created (:class:`datetime.datetime`): The datetime
                when the task instance was created.
            datetime_finished (:class:`datetime.datetime`): The datetime
                when the task instance finished.
            arguments (dict): The arguments the task instance was run
                with.
        """
        # Call the base model constructor
        super(BaseTaskInstance, self).__init__(_client)

        self.name = name
        self.uuid = uuid
        self.user = user
        self.task_queue = task_queue
        self.task_type = task_type
        self.datetime_created = datetime_created
        self.datetime_finished = datetime_finished
        self.arguments = arguments
