
{{ cookiecutter.project_name }}
{{ "=" * (cookiecutter.project_name|length) }}

pytest-httpserver is a python package which allows you to start a real HTTP server
for your tests. The server can be configured programmatically to how to respond to
requests.

The aim of this project is to provide an easy to use API to start the server, configure
the request handlers and then shut it down gracefully. All of these without touching
a configuration file or dealing with daemons.

As the HTTP server is spawned in a different thread and listening on a TCP port, you
can use any HTTP client. This library also helps you migrating to a different HTTP
client library without the need to re-write any test for your client application.

This library can be used with pytest in the most convenient way but if you prefer to use
other test frameworks, you can still use it with the context API or by writing a wrapper
for it.


Example
-------

.. code:: python

    import foo

    def some_code(foo.bar):
        pass


For further details, please read the :doc:`guide` or the :doc:`api`.

.. toctree::
    :maxdepth: 2

    guide
    api
    changes
