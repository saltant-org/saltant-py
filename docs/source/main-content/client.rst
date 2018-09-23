Client
======

.. highlight:: python

There are two ways to instantiate a saltant client:

1. Having it read settings from your environment
2. Giving it settings directly

For (1), you need to have environment variables ``SALTANT_API_URL`` and
``SALTANT_AUTH_TOKEN`` defined; once you do, you can instantiate a
client like so::

    from saltant.client import from_env

    my_client = from_env()

For (2), you supply the API URL and auth token directly::

    from saltant.client import Client

    my_client = Client(
        base_api_url='https://shahlabjobs.ca/api/',
        auth_token='p0gch4mp101fy451do9uod1s1x9i4a')

Client reference
----------------

.. autoclass:: saltant.client.Client
    :members:
    :undoc-members:
