.. _api-anymodule:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::AnyModule
*************

A module is a way to organise your code.

A module can contain:

- function definitions
- factories for structures and objects
- constants

.. warning::
  Constants are a work in progress. This needs a protocol change.

Modules are cross-language, you can define a module in C++ and use it in python or the reverse.
They can be used at runtime, so you can import a module and use it without knowing it previously.


Summary
-------

.. cpp:brief::

Detailed Description
--------------------

Creating a C++ Module
+++++++++++++++++++++

Lets create a simple foo module, with a Foo class and an egg function.

Here is the content of foo.cpp:

.. code-block:: cpp

  #include <qi/session.hpp>
  #include <qi/anymodule.hpp>

  using namespace qi;

  //the foo class takes a SessionPtr as parameter
  class Foo {
  public:
    Foo(const SessionPtr& session)
      : _session(session)
    {}

    void bar() {
    }

  private:
    SessionPtr _session;
  };
  QI_REGISTER_OBJECT(Foo, bar);

  //a simple egg function
  void eggFun() {
  }

  void register_foo_module(qi::ModuleBuilder* mb) {
    mb->advertiseMethod("egg", &eggFun);
    mb->advertiseFactory<Foo, const SessionPtr&>("Foo");
  }
  QI_REGISTER_MODULE("foo", &register_foo_module);



Now let us write a CMakeLists.txt to compile it:

.. code-block:: cmake

  cmake_minimum_required(VERSION 2.8)
  project(foo-module)
  find_package(qibuild)
  find_package(qimodule)
  qi_sanitize_compile_flags(HIDDEN_SYMBOLS)

  qi_create_module(foo SRC foo.cpp)

You can inspect your module content using qicli:

.. code-block:: sh

  qicli mod foo

Using a Module in C++
+++++++++++++++++++++

Let's create a simple binary that will load the foo module, instanciate a Foo object and register it as a "Foo" service.

footest.cpp content:

.. code-block:: cpp

  #include <qi/applicationsession.hpp>
  #include <qi/anymodule.hpp>

  using namespace qi;

  int main(int argc, char** argv) {
    ApplicationSession app(argc, argv);

    //connect the session
    app.start();

    // Register the Foo object as a service
    // loadService will automatically give the session as the first parameter
    // of the foo.Foo factory.
    app.session()->loadService("foo.Foo");

    // Then simply run the application (wait for it to end)
    app.run();
  }

Or the same code done by hand.

.. code-block:: cpp

  #include <qi/applicationsession.hpp>
  #include <qi/anymodule.hpp>

  using namespace qi;

  int main(int argc, char** argv) {
    ApplicationSession app(argc, argv);

    //connect the session
    app.start();

    // Register the module on the session by hand
    // import the module
    AnyModule foomod = qi::import("foo");
    // create a Foo object
    AnyObject ao = foomod.call<AnyObject>("Foo", app.session());
    // register the object on the Session with the name "Foo"
    app.session()->registerService("Foo", ao);


    // Then simply run the application (wait for finish)
    app.run();
  }

Let's add a line in the CMakeLists.txt to create a binary:

.. code-block:: cmake

  qi_create_bin(footest footest.cpp DEPENDS QI)

To try your new Foo service you can start it as a standalone session

.. code-block:: shell

  footest --qi-standalone

  #if you would like to register it on a running session then do
  footest --qi-url=tcp://<myip>:port

Finally you can use qicli info to inspect your module

.. code-block:: shell

  qicli info Foo


Module Factory (advanced)
+++++++++++++++++++++++++

Module support is language specific. For each language a module factory plugin should be written.

The plugin should provide a module factory function and register it using a macro. It receives a `ModuleInfo` which is the module to load and must return the loaded module.

.. code-block:: cpp

  AnyModule mylangModuleFactory(const qi::ModuleInfo& moduleInfo);

  QI_REGISTER_MODULE_FACTORY_PLUGIN("mylang", &mylangModuleFactory);


Finding Modules (advanced)
++++++++++++++++++++++++++

To find modules, the import function will start by looking at \*.mod files in share/qi/module.
This file indicates which module factory to use. From this module factory, a `ModuleInfo` is constructed and given to the right language factory function that should return a valid `AnyModule`.

Reference
---------
.. cpp:autoclass:: qi::ModuleInfo
.. cpp:autoclass:: qi::ModuleBuilder
.. cpp:autoclass:: qi::AnyModule

.. cpp:autofunction:: qi::import
.. cpp:autofunction:: qi::listModules
