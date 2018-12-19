Managers
========

.. highlight:: python

After you've instantiated a :py:class:`saltant.client.Client`, you can
interface with saltant models through managers, which are attributes of
the ``Client`` class; that is,

+ ``Client.container_task_instances``
+ ``Client.container_task_types``
+ ``Client.executable_task_instances``
+ ``Client.executable_task_types``
+ ``Client.task_queues``
+ ``Client.task_whitelists``
+ ``Client.users``

With these managers you can perform the usual API requests, along with
some other convenience functions: for example, waiting for a task
instance to finish.

Manager references
------------------

.. autoclass:: saltant.models.container_task_instance.ContainerTaskInstanceManager
    :members:

.. autoclass:: saltant.models.container_task_type.ContainerTaskTypeManager
    :members:

.. autoclass:: saltant.models.executable_task_instance.ExecutableTaskInstanceManager
    :members:

.. autoclass:: saltant.models.executable_task_type.ExecutableTaskTypeManager
    :members:

.. autoclass:: saltant.models.task_queue.TaskQueueManager
    :members:

.. autoclass:: saltant.models.task_whitelist.TaskWhitelistManager
    :members:

.. autoclass:: saltant.models.user.UserManager
    :members:
