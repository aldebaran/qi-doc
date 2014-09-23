.. _api-atomic:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::Atomic
**********

`qi::Atomic` provides support for atomic values, similarly to boost::atomic but
with simpler methods.

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

`qi::Atomic` comes with some macros to do one-time initializations in a
thread-safe manner.

Atomic Operations
.................

An atomic variable allows some operations to be atomic in a multithreaded
environment.

.. code-block:: cpp

  #include <qi/atomic.hpp>

  qi::Atomic<int> var = 0;

  void myFunction()
  {
    if (var.setIfEquals(0, 1))
      std::cout << "Set to one!";
  }

  int main()
  {
    boost::thread(myFunction);
    boost::thread(myFunction);
    boost::thread(myFunction);

    qi::os::msleep(100);
  }

This program will always print "Set to one!" once, since only one setIfEquals
can succeed. All methods in `qi::Atomic` are atomic and thus threadsafe, they
all provide a total ordering of operations.

QI_ONCE
.......

.. code-block:: cpp

  void myFunction()
  {
    QI_ONCE(std::cout << "first initialization" << std::endl);
    std::cout << "doing stuff" << std::endl;
  }

In this code, you have two guarantees:
- "first initialization" will be written only once
- "doing stuff" will never appear before "first initialization"

`QI_ONCE` is optimized so that further calls after initialization have the less
overhead possible.

You can also put multiple instructions in a `QI_ONCE`.

.. code-block:: cpp

  QI_ONCE(
      doStuff();
      doMoreStuff();
      );

This macro is only useful in C++03 and the function above may be written in
C++11:

.. code-block:: cpp

  void myFunction()
  {
    static std::once_flag flag;
    std::call_once(flag,
        [](){std::cout << "first initialization" << std::endl;});
    std::cout << "doing stuff" << std::endl;
  }

QI_THREADSAFE_NEW
.................

`QI_THREADSAFE_NEW` is there to provide a safe static initialization of
variables in C++03. Its most common use case is the following:

.. code-block:: cpp

  static std::vector<int> vec;

  void threadSafeFunction()
  {
    static boost::mutex* mutex; // = 0 is optional
    QI_THREADSAFE_NEW(mutex);
    boost::mutex::scoped_lock l(*mutex);
    vec.push_back(0);
  }

Using a simple `static boost::mutex` does not guarantee safe initialization in
a multithreaded environment in C++03 (even though GCC's implementation is
safe), that's why `QI_THREADSAFE_NEW` is needed.

In C++11, the following is safe:

.. code-block:: cpp

  static std::vector<int> vec;

  void threadSafeFunction()
  {
    static boost::mutex mutex;
    boost::mutex::scoped_lock l(mutex);
    vec.push_back(0);
  }

Reference
---------

.. cpp:autoclass:: qi::Atomic
