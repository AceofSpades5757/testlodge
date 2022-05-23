Authentication
==============

The API uses an email, API key, and account ID which must all be specified on
instantiation.

A good way to store this information for a session is to use environment
variables.

* Email: ``TESTLODGE_EMAIL``
* API Key: ``TESTLODGE_API_KEY``
* Account ID: ``TESTLODGE_ACCOUNT_ID``

.. code-block:: python

  import os

  from testlodge import Client


  tl = Client(
      email=os.environ['TESTLODGE_EMAIL'],
      api_key=os.environ['TESTLODGE_API_KEY'],
      account_id=os.environ['TESTLODGE_ACCOUNT_ID'],
  )
