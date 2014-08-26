.. _api-py-signal:

qi.Signal API
*************

Introduction
============

Signal allows communication between threads. One thread emits events, other threads register callback to the signal, and process the events appropriately.

.. warning::

  In Python services, signals must be created before registering the service on
  the session.

A type can be specified in the constructor of the signal, otherwise any value is supported.

.. warning::

  ``disconnect`` is a blocking method which will wait for the callback to
  finish (except if it's called from withing the callback). The signal
  destruction is also blocking. These two cases may cause deadlocks in your
  code, be careful.

Reference
=========

.. autoclass:: qi.Signal
   :members:


   .. py:method:: (*args)

      trigger the signal. for example:

      .. code-block:: python

        s = qi.Signal()
        s(42)
        s(42, 43)


Examples
========

.. code-block:: python

  import qi

  def onSignal(value):
    print "signal value:", value

  s = qi.Signal()

  s.connect(onSignal)
  #trigger the signal
  s(42)
