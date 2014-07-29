.. _api-dynamicobjectbuilder:
.. cpp:namespace:: qi::DynamicObjectBuilder
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::DynamicObjectBuilder
************************

This builder works similarily to the `qi::ObjectTypeBuilder`, but does not
register types to the type system (there is no type in a C++ sense). It can
only create type-erased objects from what has been advertised.

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

To build a dynamic object, advertise all its members in the builder and call
`object()` to make an object of this type.

.. code-block:: cpp

  #include <qi/type/dynamicobjectbuilder.hpp>

  void myfunc()
  {
    std::cout << "Hello world\n";
  }

  // initialize the builder
  qi::DynamicObjectBuilder builder;
  builder.advertiseMethod("myMethod", &myfunc);
  builder.advertiseSignal<int>("signal");

  // build objects
  qi::AnyObject obj = builder.object();
  obj.call<void>("myMethod");
  obj.connect("signal", &myhandler);
  obj.post("signal", 12);

Reference
---------

.. cpp:autoclass:: qi::DynamicObjectBuilder
