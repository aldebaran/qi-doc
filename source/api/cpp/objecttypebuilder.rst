.. _api-objecttypebuilder:
.. cpp:namespace:: qi::ObjectTypeBuilder
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::ObjectTypeBuilder
*********************

This builder is used to register C++ objects to the type system.

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

To use it, instanciate it, register all the members of your class and call
`registerType`.

.. code-block:: cpp

  qi::ObjectTypeBuilder<MyClass> builder;
  builder.advertise("doSomething", &MyClass::doSomething);
  builder.advertise("signal", &MyClass::signal);
  builder.advertise("property", &MyClass::property);
  builder.registerType();

Look at the :ref:`type registering
guide<guide-cxx-register-types-object-manual>` for a more complete example, and
support for overloaded functions.

Reference
---------

.. cpp:autoclass:: qi::ObjectTypeBuilder
