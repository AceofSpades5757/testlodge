Quickstart
==========

.. warning::

    Some interfaces may not yet be publically available.


Here's a simple example to start you off.

To set the stage, you want to create a new test case and upload it.

First, we need to initialize the client. So we set our credentials to environment variables to keep them relatively safe. By using ``tl`` we avoid clobbering the ``testlodge`` package name and allow some brevity in our code to cut down on keystrokes.

.. code-block:: python

  import os

  from testlodge import Client


  tl = Client(
      email='my.email@email.com',
      api_key=os.environ['TESTLODGE_API_KEY'],
      account_id=os.environ['TESTLODGE_ACCOUNT_ID'],
  )

Next, we create the new test case. A new one only needs a few items.

.. code-block:: python

  from testlodge import Case


  case = Case(
      title="Create QA Resource",
      description="Create a new resource to ensure that route is working correctly.",
      steps="1. Go to the homepage.\n2. Select the *next* item from the **Menu** box.\n3. **Create** the resource.",
      expected_results="Resource is created correctly.",
  )

Given our new case, we can upload to our TestLodge account.

.. code-block:: python

    # A return value of the case just created.
    # Includes the ID for your new test case!
    # Any errors during creation will raise an Exception
    result_case = tl.create_case(case)
