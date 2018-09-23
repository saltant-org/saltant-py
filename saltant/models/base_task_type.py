"""Base class for task type models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import dateutil.parser
from saltant.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from .resource import Model, ModelManager


class BaseTaskType(Model):
    """Base model for a task type.

    Attributes:
        id (int): The ID of the task type.
        name (str): The name of the task type.
        description (str): The description of the task type.
        user (str): The user associated with the task type.
        datetime_created (:class:`datetime.datetime`): The datetime when
            the task type was created.
        command_to_run (str): The command to run to execute the task.
        environment_variables (list): The environment variables required
            on the host to execute the task.
        required_arguments (list): The argument names for the task type.
        required_arguments_default_values (dict): Default values for the
            tasks required arguments.
        manager (:class:`saltant.models.base_task_type.BaseTaskTypeManager`):
            The task type manager which spawned this task type. This is
            used to add a put method to the task type instance.
    """
    def __init__(
            self,
            id,
            name,
            description,
            user,
            datetime_created,
            command_to_run,
            environment_variables,
            required_arguments,
            required_arguments_default_values,
            manager,):
        """Initialize a task type.

        Args:
            id (int): The ID of the task type.
            name (str): The name of the task type.
            description (str): The description of the task type.
            user (str): The user associated with the task type.
            datetime_created (:class:`datetime.datetime`): The datetime
                when the task type was created.
            command_to_run (str): The command to run to execute the task.
            environment_variables (list): The environment variables
                required on the host to execute the task.
            required_arguments (list): The argument names for the task type.
            required_arguments_default_values (dict): Default values for
                the tasks required arguments.
            manager (:class:`saltant.models.base_task_type.BaseTaskTypeManager`):
                The task type manager which spawned this task type. This
                is used to add a put method to the task type instance.
        """
        self.id = id
        self.name = name
        self.description = description
        self.user = user
        self.datetime_created = datetime_created
        self.command_to_run = command_to_run
        self.environment_variables = environment_variables
        self.required_arguments = required_arguments
        self.required_arguments_default_values = (
            required_arguments_default_values)
        self.manager = manager

    def __str__(self):
        """String representation of the task type."""
        return "%s (%s)" % (self.name, self.user)

    def put(self):
        """Updates this task type on the saltant server.

        Returns:
            :class:`saltant.models.base_task_type.BaseTaskType`:
                A task queue model instance representing the task queue
                just updated.
        """
        return self.manager.put(self)


class BaseTaskTypeManager(ModelManager):
    """Base manager for task types.

    Attributes:
        _client (:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list task types.
        detail_url (str): The URL format to get specific task types.
        model (:class:`saltant.models.resource.Model`): The model of the
            task type being used.
    """
    model = BaseTaskType

    def get(self, id=None, name=None):
        """Get a task type.

        Either the id xor the name of the task type must be specified.

        Args:
            id (int, optional): The id of the task type to get.
            name (str, optional): The name of the task type to get.

        Returns:
            :class:`saltant.models.base_task_type.BaseTaskType`:
                A task type model instance representing the task type
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
            return super(BaseTaskTypeManager, self).get(id=id)

        # Try getting the task type by name
        return self.list(filters={"name": name})[0]

    def create(
            self,
            name,
            command_to_run,
            description="",
            environment_variables=None,
            required_arguments=None,
            required_arguments_default_values=None,
            extra_data_to_post=None,):
        """Create a task type.

        Args:
            name (str): The name of the task.
            command_to_run (str): The command to run to execute the task.
            description (str, optional): The description of the task type.
            environment_variables (list, optional): The environment
                variables required on the host to execute the task.
            required_arguments (list, optional): The argument names for
                the task type.
            required_arguments_default_values (dict, optional): Default
                values for the tasks required arguments.
            extra_data_to_post (dict, optional): Extra key-value pairs
                to add to the request data. This is useful for
                subclasses which require extra parameters.

        Returns:
            :class:`saltant.models.base_task_instance.BaseTaskType`:
                A task type model instance representing the task type
                just created.
        """
        # Set None for optional list and dicts to proper datatypes
        if environment_variables is None:
            environment_variables = []

        if required_arguments is None:
            required_arguments = []

        if required_arguments_default_values is None:
            required_arguments_default_values = {}

        # Create the object
        request_url = self._client.base_api_url + self.list_url
        data_to_post = {
            "name": name,
            "description": description,
            "command_to_run": command_to_run,
            "environment_variables": json.dumps(environment_variables),
            "required_arguments": json.dumps(required_arguments),
            "required_arguments_default_values":
                json.dumps(required_arguments_default_values),
        }

        # Add in extra data if any was passed in
        if extra_data_to_post is not None:
            data_to_post.update(extra_data_to_post)

        response = self._client.session.post(request_url, data=data_to_post)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_201_CREATED,)

        # Return a model instance representing the task type
        return self.response_data_to_model_instance(response.json())

    def put(self, task_type, extra_data_to_put=None):
        """Updates a task type on the saltant server.

        Args:
            task_type (:class:`saltant.models.base_task_type.BaseTaskType`):
                A :class:`saltant.models.base_task_type.BaseTaskType`
                subclass instance to be used for updating the
                corresponding model instance on the saltant server.
            extra_data_to_put (dict, optional): Extra key-value pairs to
                add to the request data. This is useful for subclasses
                which require extra parameters.

        Returns:
            :class:`saltant.models.base_task_type.BaseTaskType`:
                A :class:`saltant.models.base_task_type.BaseTaskType`
                subclass instance representing the task type just
                updated.
        """
        # Update the object
        request_url = (
            self._client.base_api_url
            + self.detail_url.format(id=task_type.id))
        data_to_put = {
            "name": task_type.name,
            "description": task_type.description,
            "command_to_run": task_type.command_to_run,
            "environment_variables": json.dumps(
                task_type.environment_variables),
            "required_arguments": json.dumps(task_type.required_arguments),
            "required_arguments_default_values": json.dumps(
                task_type.required_arguments_default_values),
        }

        # Add in extra data if any was passed in
        if extra_data_to_put is not None:
            data_to_put.update(extra_data_to_put)

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
        """Convert response data to a task type model.

        Args:
            response_data (dict): The data from the request's response.

        Returns:
            :class:`saltant.models.base_task_type.BaseTaskType`:
                A model instance representing the task type from the
                reponse data.
        """
        # Coerce datetime strings into datetime objects
        response_data['datetime_created'] = (
            dateutil.parser.parse(response_data['datetime_created']))

        # Instantiate a model for the task instance
        return super(
            BaseTaskTypeManager,
            self).response_data_to_model_instance(response_data)
