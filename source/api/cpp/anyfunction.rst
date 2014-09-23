.. _api-anyfunction:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::AnyFunction
***************

This class is a type-erased pointer to a function. It has value semantics.

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

It is possible to create a `qi::AnyFunction` from any functor (including
``boost::function``). By using fromDynamicFunction, you can provide a
"variadic" function that will receive a vector of references to its arguments.

.. code-block:: cpp

  qi::AnyFunction freeFunc = qi::AnyFunction::from(someFunc);
  qi::AnyFunction memberFunc = qi::AnyFunction::from(Class::func, myObj);
  // if you use boost::bind or qi::bind, you must explicitely cast to the right
  // signature
  qi::AnyFunction memberFunc = qi::AnyFunction::from(
      boost::function<int(int value1, const std::string& value2)>(
        boost::bind(someFunc, _1, "argument")));

You can then call the function with a vector of arguments or by giving the
arguments as in a normal function call.

.. warning::

  The caller is responsible for destroying its `qi::AnyReference` to the
  returned value when using type-erased calls. You can store the returned
  reference in a `qi::AnyValue` to benefit from RAII destruction.

.. code-block:: cpp

  // typed call
  int value = func.call<int>(42);

  // using operator()
  qi::AnyValue ret(func(42), false, true);
  std::cout << ret.toInt() << std::endl;

  // type-erased call
  qi::AnyReferenceVector args;
  args.push_back(qi::AnyReference::from(42));
  ret.reset(func.call(args), false, true);

Reference
---------

.. cpp:autotypedef:: qi::DynamicFunction

.. cpp:autoclass:: qi::AnyFunction
