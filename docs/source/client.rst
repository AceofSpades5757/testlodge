Client
======

The clients is the top-level interface representing your connection with the
TestLodge API.

.. code-block:: python

  import os

  from testlodge import Client


  tl = Client(
      email='my.email@email.com',
      api_key=os.environ['TESTLODGE_API_KEY'],
      account_id=os.environ['TESTLODGE_ACCOUNT_ID'],
  )
