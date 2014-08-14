.. _api-preproc:

qi preprocessor macros
**********************

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

Variadic Templates
^^^^^^^^^^^^^^^^^^

Overview
........

libqi provides macros to emulate C++11 variadic templates. The idea is to
transform a variadic definition:

.. code-block:: cpp

  template <typename R, typename... T>
  R forward(T... args) {
    return call<R, T...>(args...);
  }

into multiple normal definitions:

.. code-block:: cpp

  template <typename R>
  R forward() {
    return call<R>();
  }

  // ...

  template <typename R, typename T1, typename T2, typename T3>
  R forward(T1 arg1, T2 arg2, T3 arg3) {
    return call<R, T1, T2, T3>(arg1, arg2, arg3);
  }

The downside is that it makes compilation time longer and does not support
arguments up to infinity.

Usage
.....

With the previous example, the macro usage looks like:

.. code-block:: cpp

  #define genCall(n, ATYPEDECL, ATYPES, ADECL, AUSE, comma)   \
    template <typename R comma ATYPEDECL>                     \
    R forward(ADECL)                                          \
    {                                                         \
      /* note that you can skip "comma ATYPES" since they can \
       * be automatically inferred in this case */            \
      return call<R comma ATYPES>(AUSE);                      \
    }
  QI_GEN(genCall)
  #undef genCall

You must define a macro that will be called with 0, 1, ..., n arguments and
must generate a definition each time.

- ``n`` is the number of arguments this call should generate.
- ``ATYPESDECL`` is the list of typenames with their names separated by commas.
- ``ATYPES`` is just the names of the template arguments.
- ``ADECL`` is the declaration of each parameter with a name.
- ``AUSE`` is the names of the parameters.
- ``comma`` is a comma when there is at least an argument, nothing otherwise.
  This is needed for the first call in which there is no template argument and
  the comma must be skipped.

Reference
---------

.. cpp:automacro:: QI_GEN
