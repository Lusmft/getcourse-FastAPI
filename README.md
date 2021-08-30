First run the following commands to bootstrap your environment with ``poetry``: ::

    git clone https://github.com/Lusmft/getcourse-FastAPI/
    cd getcourse-FastAPI
    poetry install
    poetry shell

Then mosify ``.env`` file in project root and set environment variables for application: ::

    touch .env
    echo DATABASE_URL=sqlite:///./database.sqlite3 >> .env
    echo JWT_SECRET=secret >> .env

To run the web application in debug use::

    uvicorn app.main:app --reload


Run tests
---------

Tests for this project are defined in the ``tests/`` folder. 

This project uses `pytest
<https://docs.pytest.org/>`_ to define tests because it allows you to use the ``assert`` keyword with good formatting for failed assertations.


To run all the tests of a project, simply run the ``pytest`` command: ::

    $ pytest
================= test session starts ==================
platform linux -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /data/data/com.termux/files/usr/bin/python3
cachedir: .pytest_cache
rootdir: /storage/emulated/0/prog/getcourse-fastapi
plugins: asyncio-0.15.1, anyio-3.3.0
collected 9 items

tests/test_app.py::test_sign_up PASSED           [ 11%]
tests/test_app.py::test_sign_up_if_user_exists PASSED [ 22%]
tests/test_app.py::test_sign_in PASSED           [ 33%]
tests/test_app.py::test_failed_sign_in PASSED    [ 44%]
tests/test_app.py::test_get_user PASSED          [ 55%]
tests/test_app.py::test_get_user_without_token PASSED [ 66%]
tests/test_app.py::test_import_deals PASSED      [ 77%]
tests/test_app.py::test_async PASSED             [ 88%]
tests/test_app.py::test_remove_db PASSED         [100%]

================== 9 passed in 8.38s ===================
    $

If you want to run a specific test, you can do this with `this
<https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests>`_ pytest feature: ::

    $ pytest tests/test_app.py::test_sign_up

Deployment with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create or modify ``.env`` file like in `Quickstart` section.
Then just run::

    docker-compose up -d app

Application will be available on ``localhost`` in your browser.

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   
    ├── models           - pydantic models for this application.
 
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
