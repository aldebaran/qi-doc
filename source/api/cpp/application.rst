.. _api-application:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::Application
***************

Application takes care of the initialisation and termination of the program.

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

`Application` is meant to be instantiated in the main function. It provides a
`run` function that keeps the application running until the user asks for
termination (usually through CTRL-C), which is useful when implementing a
service.

`Application`'s destructor blocks until there is no more work scheduled in the
eventloop and all sockets are closed.

.. seealso:: You rarely need to use this class, see `ApplicationSession`.

Usage Example
=============

.. code-block:: cpp

  #include <qi/application.hpp>

  int main(int argc, char* argv[])
  {
    qi::Application app(argc, argv);

    // do things

    app.run();
  }

Reference
---------

.. cpp:autoclass:: qi::Application

.. cpp:automacro:: QI_AT_ENTER
.. cpp:automacro:: QI_AT_EXIT
