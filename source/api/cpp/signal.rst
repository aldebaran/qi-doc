.. _api-signal:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::Signal
**********

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

This is an implementation of the *signal/event* paradigm, with some
specificities:

- Thread-safe.
- Synchronous or asynchronous subscriber invocation.
- Subscriber disconnection garantees that subscriber is not/will not be called
  anymore when it returns.
- Automatic subscriber disconnection when ``weak_ptr`` or `qi::Trackable` is
  used.

`qi::Signal` is non-copiable.

Template arguments
==================

`Signal` is templated by the argument types that must be passed when
triggering, and that will be transmitted to subscribers. For instance,
``Signal<int, int>`` is the type of a `Signal` with two ints as payload type:
`Signal::operator()` will expect two ints, and subscribers will be expected to
have signature ``void(int, int)``.

.. note::

  The types used as template arguments to signal must be registered to the type
  system. If you fail to do that, you will get errors like::

    Cannot do 'clone' on YourType

Connection to a signal
======================

Use `Signal::connect` to register a subscriber that will be called each time
the signal is triggered.

Arguments to `connect` can take multiple forms:

- A function or callable object (like ``boost::function``).
- A function or callable, followed by arguments and placeholders that will be
  bound to the function (more about that below).
- Another compatible `Signal`.

The variadic form of `connect` works in a similar manner to
``boost::bind()``: values passed to `connect` will be passed to the function,
in order, and placeholders ``_1``, ``_2``... will be replaced by the signal
payloads.

This form will also recognize if the first argument is a ``boost::weak_ptr``,
or if it as pointer to a class inheriting from `qi::Trackable`. In both cases,
the subscriber will be automatically disconnected if the pointer cannot be
locked. See :ref:`this example<future-connect>` for a demonstration of that
very same mechanism in `qi::Future`.

`Signal::connect` returns a ``SignalSubscriber&``, that you can use to:

- Override the default call type for this subscriber to synchronous or
  asynchronous by calling `SignalSubscriber::setCallType` (see :ref:`callback
  type<signal-setCallType>`).
- Obtain a subscriber identifier of type `qi::SignalLink` by casting the
  `SignalSubscriber`:

.. code-block:: cpp

  qi::SignalLink l = someSignal.connect(callback1);

Unregistering a subscriber is done by invoking `Signal::disconnect` with a
`SignalLink` as its sole argument. The call will block until all currently
running invocations of the subscriber have finished. This gives you the strong
guarantee than once `disconnect` has returned, your callback function is not
being called, and will never be called again.

.. warning::

  `disconnect` is a blocking method which will wait for the callback to finish
  (except if it's called from withing the callback). The signal destruction is
  also blocking. These two cases may cause deadlocks in your code, be careful.

Triggering the signal
=====================

Triggering the signal is achieved by using the `Signal::operator()`, with
arguments matching the `Signal` type:

.. code-block:: c++

  qi::Signal<int, int> sig;
  sig(51, 42);

This will invoke all subscribers with given arguments.

.. _signal-setCallType:

Signal callback type
====================

It is possible to control how subscribers are invoked:

- `MetaCallType_Auto` is the default and means asynchronous.
- `MetaCallType_Direct` forces a synchronous call.
- `MetaCallType_Queued` forces an asynchronous call.

Note that if any subscriber is invoked asynchronously, the arguments passed to
`Signal::operator()` will be copied.

You can set the call type of a signal globally with `setCallType`, but you can
also set it per-callback. You can do that by calling ``setCallType`` on the
`SignalSubscriber` returned by `connect`.

.. code-block:: cpp

  qi::SignalLink l = someSignal
      .connect(callback2)
      .setCallType(qi::MetaCallType_Direct);

.. warning::

  It is *very dangerous* to set the call type to Direct as your function may
  block the code that triggers the signal. This type of call is only useful for
  optimization purposes, only for very small and fast fuctions that do not
  lock.

Signal lazy enabling
====================

Sometimes, mainly for performance reasons, it is useful to only enable some
code if a `Signal` has at least one subscriber. For example, if you have a
signal ``humanDetected``, you may want to enable the image processing code only
if there is at least one subscriber to the signal to save CPU cycles.

This can be achieved by passing a callback to the `Signal` constructor, of
signature ``void(bool)``.  This function will be called *synchronously* each
time the number of subscribers switches between 0 and 1.

.. code-block:: cpp

  void onConnect(bool c)
  {
    if (c)
      std::cout << "There is at least one connection";
    else
      std::cout << "There is no more connection";
  }

  qi::Signal sig(onConnect);
  qi::SignalLink l1 = sig.connect(mycallback); // calls onConnect(true)
  qi::SignalLink l2 = sig.connect(mycallback);
  sig.disconnect(l1);
  sig.disconnect(l2); // calls onConnect(false);

Overriding signal triggering behavior (advanced)
================================================

Sometimes, mainly when bridging `Signal` with another signal implementation,
one needs to override the action performed when the signal is triggered (which
is by default to invoke all subscribers).

This can be achieved by inheriting from `Signal`, and then either overriding
the `trigger` virtual function, or by calling `setTriggerOverride` with a
functor that will replace the original trigger. You can then call
`callSubscribers` to invoke the subscribers, which ``trigger`` would do
by default.

Reference
---------

.. cpp:autoclassinherits:: qi::Signal, qi::SignalF, qi::SignalBase

.. cpp:autoclass:: qi::SignalSubscriber
