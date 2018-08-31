"""Base class for executable task instance model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import dateutil.parser
from saltant.constants import HTTP_200_OK
from .base_task_instance import (
    BaseTaskInstance,
    BaseTaskInstanceManager,
)


class ExecutableTaskInstanceManager(BaseTaskInstanceManager):
    """Base manager for task instances.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task instances.
        detail_url (str): The URL format to get specific task instances.
    """
    list_url = 'executabletaskinstances/'
    detail_url = 'executabletaskinstances/{uuid}/'

    def get(self, uuid):
        """Get the task instance.

        Args:
            uuid (str): The UUID of the task instance to get.

        Returns:
            :class:`saltant.models.executable_task_instance.ExecutableTaskInstance`:
                An ExecutableTaskInstance model instance representing
                the task instance.
        """
        # Get the object
        request_url = (
            self._client.base_api_url
            + self.detail_url.format(uuid=uuid))

        response = self._client.session.get(request_url)

        # Validate that the request was successful
        self.validate_request_success(
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_200_OK,)

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
    pass
