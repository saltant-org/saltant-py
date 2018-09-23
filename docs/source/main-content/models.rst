Models
======

.. highlight:: python

saltant model instances are repesented with model classes in saltant-py.
These model classes have saltant model instance attributes as class
attributes (e.g., UUIDs for task instances).

For some models, notably, the task instance models, there are
convenience methods for, in the case of task instances, cloning,
terminating, and waiting until completion.

Model references
----------------

.. autoclass:: saltant.models.container_task_instance.ContainerTaskInstance
    :members:

.. autoclass:: saltant.models.container_task_type.ContainerTaskType
    :members:

.. autoclass:: saltant.models.executable_task_instance.ExecutableTaskInstance
    :members:

.. autoclass:: saltant.models.executable_task_type.ExecutableTaskType
    :members:

.. autoclass:: saltant.models.task_queue.TaskQueue
    :members:

.. autoclass:: saltant.models.user.User
    :members:
