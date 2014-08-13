.. _api-py-future:

qi.Future API
*************

Introduction
============

Promise and Future are a way to synchronise data between multiples threads.
The number of future associated to a promise is not limited.
Promise is the setter, future is the getter.
Basically, you have a task to do, that will return a value, you give it a Promise.
Then you have others thread that depend on the result of that task, you give them future
associated to that promise, the future will block until the value or an error is set
by the promise.


Reference
=========

.. py:data:: qi.FutureState

  Constants that describe the state of the Future.
  This is the status returned by :py:meth:`qi.Future.wait`

  ================================    ====================================================
  qi.FutureState.None                 The future is not bound.
  qi.FutureState.Running              The future is attached to a Promise.
  qi.FutureState.Canceled             The future has been canceled
  qi.FutureState.FinishedWithError    The future has finished and an error is available
  qi.FutureState.FinishedWithValue    The future has finished and a value is available
  ================================    ====================================================


.. py:data:: qi.FutureTimeout

  Constants to use for timeout arguments.

  ================================    ====================================================
  qi.FutureTimeout.None               Do not wait.
  qi.FutureTimeout.Infinite           Block forever
  ================================    ====================================================

.. autoclass:: qi.Promise
   :members:

   ..   method:: __init__(cb)

     :param cb: a python callable

     If the promise was constructed with a callback in parameter, it will be executed
     when a future associated to the promise is cancelled.
     The first argument of the callback is the promise itself.

.. autoclass:: qi.Future
   :members:

Examples
========

Simple example:

.. code-block:: python

  import qi
  import time
  import threading

  def doSomeWork(p):
    #do your work here instead of sleeping
    time.sleep(1)
    p.setValue(42)

  p = qi.Promise()
  f = p.future()
  threading.Thread(target=doSomeWork, args=[p]).start()
  print "result:", f.value()

With callback:

.. code-block:: python

  import qi
  import time
  import threading

  def doSomeWork(p):
    #do your work here instead of sleeping
    time.sleep(1)
    p.setValue(42)

  def resultReady(f):
    if f.hasValue():
      print "Value:", f.value()
    elif f.hasError():
      print "Error:", f.error()

  p = qi.Promise()
  f = p.future()
  threading.Thread(target=doSomeWork, args=[p]).start()

  #resultReady will be called even if the result is already there.
  f.addCallback(resultReady)

Cancellation support
====================

In some situations, you will want to create asynchronous operations that can be
interrupted in the middle of their execution. For that you can set a callback
to the promise that will be called when someone asks for cancellation. You
usually don't need anything particular in this callback and you can just check
for ``isCancelRequested()`` on the promise.

.. code-block:: python

  import qi
  import time
  from functools import partial

  class FakeOperation:
      def doStep(self):
          time.sleep(0.3)
          print 'I executed one step'

      def longOperation(self, promise):
          "do steps or cancel before the end"
          for i in range(10):
              if promise.isCancelRequested():
                  print 'Cancel requested, aborting'
                  promise.setCanceled()
                  return
              self.doStep()
          # if an error occured, promise.setError("error")
          # use setValue if everything went ok
          print 'longOperation finished'
          promise.setValue(None)

      def asyncLongOperation(self):
          "start long operation and return a cancelable future"
          promise = qi.Promise(qi.PromiseNoop)
          qi.async(partial(self.longOperation, promise))
          return promise.future()

  m = FakeOperation()

  fut = m.asyncLongOperation()
  time.sleep(1)
  fut.cancel()

  assert fut.wait() == qi.FutureState.Canceled
  assert fut.isCanceled()
  assert fut.isFinished()

.. autofunction:: qi.PromiseNoop
