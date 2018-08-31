"""Base class for executable task instance model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import dateutil.parser
from saltant.constants import HTTP_200_OK
from saltant.exceptions import BadHttpRequestError
from .base_task_instance import (
    BaseTaskInstance,
    BaseTaskInstanceManager,
)


class ExecutableTaskInstanceManager(BaseTaskInstanceManager):
    """Base manager for task instances.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
    """
    def get(self, uuid):
        # Get the object
        request_url = (
            self._client.base_api_url
            + 'executabletaskinstances/{uuid}/'.format(uuid=uuid))

        response = self._client.session.get(request_url)

        # Validate
        try:
            assert response.status_code == HTTP_200_OK
        except AssertionError:
            msg = "Request to {} failed with status {}".format(
                request_url,
                response.status_code)
            raise BadHttpRequestError(msg)

        # Coerce datetime strings into datetime objects
        response_data = response.json()
        response_data['datetime_created'] = (
            dateutil.parser.parse(response_data['datetime_created']))

        if response_data['datetime_finished']:
            response_data['datetime_finished'] = (
                dateutil.parser.parse(response_data['datetime_finished']))

        # Instantiate a model for the task instacne
        return ExecutableTaskInstance(**response_data)



class ExecutableTaskInstance(BaseTaskInstance):
    """Model for an executable task instance.

    Attributes:
:       name (str): The name of the task instance.
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
    pass
