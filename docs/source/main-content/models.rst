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

    .. automethod:: __init__

.. autoclass:: saltant.models.container_task_type.ContainerTaskType
    :members:

    .. automethod:: __init__

.. autoclass:: saltant.models.executable_task_instance.ExecutableTaskInstance
    :members:

    .. automethod:: __init__

.. autoclass:: saltant.models.executable_task_type.ExecutableTaskType
    :members:

    .. automethod:: __init__

.. autoclass:: saltant.models.task_queue.TaskQueue
    :members:

    .. automethod:: __init__

.. autoclass:: saltant.models.user.User
    :members:

    .. automethod:: __init__
