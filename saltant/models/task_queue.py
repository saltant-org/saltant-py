"""Classes for task queue model and manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from saltant.constants import HTTP_200_OK, HTTP_201_CREATED
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
        runs_executable_tasks (bool): A Boolean specifying whether the
            queue runs executable tasks.
        runs_docker_container_tasks (bool): A Boolean specifying whether
            the queue runs container tasks that run in Docker
            containers.
        runs_singularity_container_tasks (bool): A Boolean specifying
            whether the queue runs container tasks that run in
            Singularity containers.
        active (bool): A Booleon signalling whether the queue is active.
        whitelists (list): A list of task whitelist IDs.
        manager (:class:`saltant.models.task_queue.TaskQueueManager`):
            The task queue manager which spawned this task queue.
    """

    def __init__(
        self,
        id,
        user,
        name,
        description,
        private,
        runs_executable_tasks,
        runs_docker_container_tasks,
        runs_singularity_container_tasks,
        active,
        whitelists,
        manager,
    ):
        """Initialize a task queue.

        Args:
            id (int): The ID of the task queue.
            user (str): The user who created the task queue.
            name (str): The name of the task queue.
            description (str): The description of the task queue.
            private (bool): A Booleon signalling whether the queue can
                only be used by its associated user.
            runs_executable_tasks (bool): A Boolean specifying whether
                the queue runs executable tasks.
            runs_docker_container_tasks (bool): A Boolean specifying
                whether the queue runs container tasks that run in
                Docker containers.
            runs_singularity_container_tasks (bool): A Boolean
                specifying whether the queue runs container tasks that
                run in Singularity containers.
            active (bool): A Booleon signalling whether the queue is
                active.
            whitelists (list): A list of task whitelist IDs.
            manager (:class:`saltant.models.task_queue.TaskQueueManager`):
                The task queue manager which spawned this task instance.
        """
        # Call the parent constructor
        super(TaskQueue, self).__init__(manager)

        # Add in task queue stuff
        self.id = id
        self.user = user
        self.name = name
        self.description = description
        self.private = private
        self.runs_executable_tasks = runs_executable_tasks
        self.runs_docker_container_tasks = runs_docker_container_tasks
        self.runs_singularity_container_tasks = (
            runs_singularity_container_tasks
        )
        self.active = active
        self.whitelists = whitelists

    def __str__(self):
        """String representation of the task queue."""
        return self.name

    def sync(self):
        """Sync this model with latest data on the saltant server.

        Note that in addition to returning the updated object, it also
        updates the existing object.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                This task queue instance after syncing.
        """
        self = self.manager.get(id=self.id)

        return self

    def patch(self):
        """Updates this task queue on the saltant server.

        This is an alias for the model's put method. (Both are identical
        operations on the model level.)

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just updated.
        """
        return self.put()

    def put(self):
        """Updates this task queue on the saltant server.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just updated.
        """
        return self.manager.put(
            id=self.id,
            name=self.name,
            description=self.description,
            private=self.private,
            runs_executable_tasks=self.runs_executable_tasks,
            runs_docker_container_tasks=self.runs_docker_container_tasks,
            runs_singularity_container_tasks=self.runs_singularity_container_tasks,
            active=self.active,
            whitelists=self.whitelists,
        )


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

    list_url = "taskqueues/"
    detail_url = "taskqueues/{id}/"
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
        if not (id is None) ^ (name is None):
            raise ValueError("Either id or name must be set (but not both!)")

        # If it's just ID provided, call the parent function
        if id is not None:
            return super(TaskQueueManager, self).get(id=id)

        # Try getting the task queue by name
        return self.list(filters={"name": name})[0]

    def create(
        self,
        name,
        description="",
        private=False,
        runs_executable_tasks=True,
        runs_docker_container_tasks=True,
        runs_singularity_container_tasks=True,
        active=True,
        whitelists=None,
    ):
        """Create a task queue.

        Args:
            name (str): The name of the task queue.
            description (str, optional): A description of the task queue.
            private (bool, optional): A boolean specifying whether the
                queue is exclusive to its creator. Defaults to False.
            runs_executable_tasks (bool, optional): A Boolean specifying
                whether the queue runs executable tasks. Defaults to
                True.
            runs_docker_container_tasks (bool, optional): A Boolean
                specifying whether the queue runs container tasks that
                run in Docker containers. Defaults to True.
            runs_singularity_container_tasks (bool, optional): A Boolean
                specifying whether the queue runs container tasks that
                run in Singularity containers. Defaults to True.
            active (bool, optional): A boolean specifying whether the
                queue is active. Default to True.
            whitelists (list, optional): A list of task whitelist IDs.
                Defaults to None (which gets translated to []).

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just created.
        """
        # Translate whitelists None to [] if necessary
        if whitelists is None:
            whitelists = []

        # Create the object
        request_url = self._client.base_api_url + self.list_url
        data_to_post = {
            "name": name,
            "description": description,
            "private": private,
            "runs_executable_tasks": runs_executable_tasks,
            "runs_docker_container_tasks": runs_docker_container_tasks,
            "runs_singularity_container_tasks": runs_singularity_container_tasks,
            "active": active,
            "whitelists": whitelists,
        }

        response = self._client.session.post(request_url, data=data_to_post)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_201_CREATED,
        )

        # Return a model instance representing the task instance
        return self.response_data_to_model_instance(response.json())

    def patch(
        self,
        id,
        name=None,
        description=None,
        private=None,
        runs_executable_tasks=None,
        runs_docker_container_tasks=None,
        runs_singularity_container_tasks=None,
        active=None,
        whitelists=None,
    ):
        """Partially updates a task queue on the saltant server.

        Args:
            id (int): The ID of the task queue.
            name (str, optional): The name of the task queue.
            description (str, optional): The description of the task
                queue.
            private (bool, optional): A Booleon signalling whether the
                queue can only be used by its associated user.
            runs_executable_tasks (bool, optional): A Boolean specifying
                whether the queue runs executable tasks.
            runs_docker_container_tasks (bool, optional): A Boolean
                specifying whether the queue runs container tasks that
                run in Docker containers.
            runs_singularity_container_tasks (bool, optional): A Boolean
                specifying whether the queue runs container tasks that
                run in Singularity containers.
            active (bool, optional): A Booleon signalling whether the
                queue is active.
            whitelists (list, optional): A list of task whitelist IDs.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just updated.
        """
        # Update the object
        request_url = self._client.base_api_url + self.detail_url.format(id=id)

        data_to_patch = {}

        if name is not None:
            data_to_patch["name"] = name

        if description is not None:
            data_to_patch["description"] = description

        if private is not None:
            data_to_patch["private"] = private

        if runs_executable_tasks is not None:
            data_to_patch["runs_executable_tasks"] = runs_executable_tasks

        if runs_docker_container_tasks is not None:
            data_to_patch[
                "runs_docker_container_tasks"
            ] = runs_docker_container_tasks

        if runs_singularity_container_tasks is not None:
            data_to_patch[
                "runs_singularity_container_tasks"
            ] = runs_singularity_container_tasks

        if active is not None:
            data_to_patch["active"] = active

        if whitelists is not None:
            data_to_patch["whitelists"] = whitelists

        response = self._client.session.patch(request_url, data=data_to_patch)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_200_OK,
        )

        # Return a model instance representing the task instance
        return self.response_data_to_model_instance(response.json())

    def put(
        self,
        id,
        name,
        description,
        private,
        runs_executable_tasks,
        runs_docker_container_tasks,
        runs_singularity_container_tasks,
        active,
        whitelists,
    ):
        """Updates a task queue on the saltant server.

        Args:
            id (int): The ID of the task queue.
            name (str): The name of the task queue.
            description (str): The description of the task queue.
            private (bool): A Booleon signalling whether the queue can
                only be used by its associated user.
            runs_executable_tasks (bool): A Boolean specifying whether
                the queue runs executable tasks.
            runs_docker_container_tasks (bool): A Boolean specifying
                whether the queue runs container tasks that run in
                Docker containers.
            runs_singularity_container_tasks (bool): A Boolean
                specifying whether the queue runs container tasks that
                run in Singularity containers.
            active (bool): A Booleon signalling whether the queue is
                active.
            whitelists (list): A list of task whitelist IDs.

        Returns:
            :class:`saltant.models.task_queue.TaskQueue`:
                A task queue model instance representing the task queue
                just updated.
        """
        # Update the object
        request_url = self._client.base_api_url + self.detail_url.format(id=id)
        data_to_put = {
            "name": name,
            "description": description,
            "private": private,
            "runs_executable_tasks": runs_executable_tasks,
            "runs_docker_container_tasks": runs_docker_container_tasks,
            "runs_singularity_container_tasks": runs_singularity_container_tasks,
            "active": active,
            "whitelists": whitelists,
        }

        response = self._client.session.put(request_url, data=data_to_put)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_200_OK,
        )

        # Return a model instance representing the task instance
        return self.response_data_to_model_instance(response.json())
