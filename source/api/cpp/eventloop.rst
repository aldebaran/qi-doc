.. _api-eventloop:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::EventLoop
*************

Provide an eventloop based on boost::asio.

Summary
=======

.. cpp:brief::

Detailed Description
====================

This eventloop consists of a threadpool of boost::asio threads waiting for
work. You can schedule work using `async` or using the ``io_service`` directly
(to do asynchronous operations on sockets for example). Most basic usages are
described in :ref:`asynchronous operations<guide-cxx-async>`.

Good use of a threadpool
------------------------

It is often needed to schedule asynchronous work so that multiple work can be
done in parallel. One way to do such a thing is to spawn a thread for the task
and have the thread quit when the task is finished. It is bad practice to do
such things. Spawning and exiting threads is costly in performance and must be
avoided.

A threadpool starts a bunch of threads at its initialization and allows one to
schedule short tasks on it, this avoids thread creations/destructions.

Blocking threads
................

It is not recommended to schedule large tasks in the threadpool (like image
or sound processing) since it will block a thread and be unfair to other users.
Such tasks should be scheduled on separate threads (which should of course not
be created/destroyed each time there is work to do) synchronized with mutexes
and condition variables.

Additionally, an asynchronous task should not lock long-held mutexes or do
blocking calls. Every time a task does that, a thread of the threadpool is
blocked an no more work can be scheduled on it until the task finishes.

Threadpool Monitoring
---------------------

The threadpool is constantly monitored by an external thread to check if it is
full (or deadlocked). The thread schedules a "ping" every 0.5 second and waits
for the "pong" for 0.5 second. If it times out, a new thread is spawned until
the maximum is reached. If 20 timeouts happen in a row, the emergency callback
is called (which may abort execution since a deadlock is likely to have
occurred).

Customizing the Threadpool Behavior
-----------------------------------

You can control how the threadpool behaves through environment variables.

- `QI_EVENTLOOP_THREAD_COUNT`: number of threads the eventloop should start
  with. By default, it will start with one thread per CPU. This is overridden
  by calling `qi::startEventLoop` explicitly.
- `QI_EVENTLOOP_MAX_THREADS`: maximum number of threads that the threadpool can
  have.
- `QI_EVENTLOOP_GRACE_PERIOD`: time in ms to wait after a failed ping, defaults
  to 0.
- `QI_EVENTLOOP_PING_TIMEOUT`: time in ms to wait for a ping response before
  considering it failed, defaults to 500.
- `QI_EVENTLOOP_MAX_TIMEOUTS`: number of timeouts before calling the emergency
  callback, defaults to 20.

Reference
=========

.. cpp:autoclass:: qi::EventLoop

.. cpp:autofunction:: qi::getEventLoop()
.. cpp:autofunction:: qi::startEventLoop(int)
.. cpp:autofunction:: qi::getIoService()
.. cpp:autofunction:: qi::async(boost::function<R()>, uint64_t)
.. cpp:autofunction:: qi::async(boost::function<R()>, qi::Duration)
.. cpp:autofunction:: qi::async(boost::function<R()>, qi::SteadyClockTimePoint)
