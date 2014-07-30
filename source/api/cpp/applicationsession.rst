.. _api-applicationsession:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::ApplicationSession
**********************

`ApplicationSession` is an application with an embedded auto-connected `Session`.

Detailed Description
--------------------

`ApplicationSession` is meant to be instantiated in the main function. It work
pretty much like `Application` but embeds a Session in it. The session is
connected when `start` is called (or when `run` is called if `start` is never
called).

The session is automatically activated (in listening or connected mode)
according to the arguments passed to the program.

.. seealso:: This class follows the logic of `Application`.

Usage Example
=============

.. code-block:: cpp

  int main(int argc, char* argv[])
  {
    qi::ApplicationSession app(argc, argv);

    app.start();

    qi::SessionPtr session = app.session();

    // do things with session->service() or session->registerService

    // if you want to keep the program running
    app.run();
  }

Summary
-------

.. cpp:brief::

Reference
---------

`qi::ApplicationSession` is here to handle qi::Application and qi::Session
auto-magically.

.. cpp:autoclass:: qi::ApplicationSession
