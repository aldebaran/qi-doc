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

.. _api-py-signal-lazyenable:

Signal lazy enabling
====================

Sometimes, mainly for performance reasons, it is useful to only enable some
code if a `Signal` has at least one subscriber. For example, if you have a
signal ``humanDetected``, you may want to enable the image processing code only
if there is at least one subscriber to the signal to save CPU cycles.

This can be achieved by passing a callback to the `Signal` constructor, which
receives a boolean as an argument. This function will be called
*synchronously* each time the number of subscribers switches between 0 and 1.

.. code-block:: python

  def onConnect(c):
      if c:
          print "There is at least one connection"
      else:
          print "There is no more connection"

  sig = qi::Signal('m', onConnect)
  l1 = sig.connect(mycallback) # calls onConnect(True)
  l2 = sig.connect(mycallback)
  sig.disconnect(l1)
  sig.disconnect(l2) # calls onConnect(False)

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
