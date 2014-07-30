.. _api-eventloop:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::EventLoop
*************

Provide an eventloop based on boost::asio.

Summary
-------

.. cpp:brief::

Reference
---------

.. cpp:autoclass:: qi::EventLoop

Functions
=========
.. cpp:autofunction:: qi::getEventLoop()
.. cpp:autofunction:: qi::startEventLoop(int)
.. cpp:autofunction:: qi::getIoService()
.. cpp:autofunction:: qi::async(boost::function<R()>, uint64_t)
