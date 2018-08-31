"""Base class for executable task instance model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from .base_task_instance import BaseTaskInstance


class ExecutableTaskInstance(BaseTaskInstance):
    """Model for an executable task instance.

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
    def refresh(self):
        """Refresh the task instance's data."""
        # TODO(mwiens91): probably call the same method you use to fetch
        # the task instance data?
        pass
