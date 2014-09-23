.. _api-clock:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::Clock
*********

Libqi provides abstractions to use clocks and express durations.

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

Libqi provides clocks based on boost clocks. They are compatible with
everything in boost::chrono.

Libqi provides two clocks:

- `WallClock` which is the system clock and may be updated (so the time may go
  backward when the user changes it)
- `SteadyClock` which is guaranteed to go only forward whatever the user does.

These clocks are an abstraction over boost::chrono's clocks so that all
durations and time points are expressed in nanoseconds regardless of the
clock's real resolution. This allows one to write code without caring about
using ``boost::chrono::duration_cast`` and makes the code cross-platform.

You can also use predefined types for durations and time points (similar to
boost ones). Keep in mind that you still need to use
``boost::chrono::duration_cast`` when you need to do a lossy cast.

.. code-block:: cpp

  qi::MicroSeconds us(188800);
  qi::MilliSeconds ms = boost::chrono::duration_cast<qi::MilliSeconds>(us);

Reference
---------

.. cpp:autotypedef:: qi::Duration
.. cpp:autotypedef:: qi::NanoSeconds
.. cpp:autotypedef:: qi::MicroSeconds
.. cpp:autotypedef:: qi::MilliSeconds
.. cpp:autotypedef:: qi::Seconds
.. cpp:autotypedef:: qi::Minutes
.. cpp:autotypedef:: qi::Hours

.. cpp:autoclass:: qi::SteadyClock

.. cpp:autoclass:: qi::WallClock

Functions
=========

.. cpp:autofunction:: qi::steadyClockNow()
.. cpp:autofunction:: qi::wallClockNow()
.. cpp:autofunction:: qi::sleepFor(const qi::Duration&)
.. cpp:autofunction:: qi::sleepUntil(const SteadyClockTimePoint&)
.. cpp:autofunction:: qi::sleepUntil(const WallClockTimePoint&)
