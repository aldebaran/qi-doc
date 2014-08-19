.. _api-log:

qi::log
*******

Summary
-------

.. cpp:brief::

Detailed Description
--------------------

`qi::log` provides logging facilities. It allows one to log in different
categories with different levels.

The user can choose which categories they want to see and at which level. It is
possible to add handlers to process the log, broadcast them on the network,
save them in a file, etc.

.. code-block:: cpp

  #include <qi/log.hpp>

  qiLogCategory("myprogram.mymodule");

  int main()
  {
    qiLogInfo() << "Hello world";

    // this variant is slower than the one above
    qiLogError("this.goes.in.another.category") << "Goodbye world";

    return 0;
  }

.. warning::

  Log calls are lazily evaluated. When you put a function call in your log
  statements, the function will *not* be called if the log is disabled (at
  runtime or compilation-time).

  .. code-block:: cpp

    int i = 0;

    int f() { ++i; return 0; }

    void g() {
      qiLogVerbose() << f(); // f() may not be called!
    }

Reference
---------

Macro
=====

.. cpp:automacro:: qiLogCategory
.. cpp:automacro:: qiLogDebug
.. cpp:automacro:: qiLogDebugF
.. cpp:automacro:: qiLogVerbose
.. cpp:automacro:: qiLogVerboseF
.. cpp:automacro:: qiLogInfo
.. cpp:automacro:: qiLogInfoF
.. cpp:automacro:: qiLogWarning
.. cpp:automacro:: qiLogWarningF
.. cpp:automacro:: qiLogError
.. cpp:automacro:: qiLogErrorF
.. cpp:automacro:: qiLogFatal
.. cpp:automacro:: qiLogFatalF


.. .. cpp:autonamespace:: qi::log

.. cpp:autoenum:: qi::LogColor
.. cpp:autoenum:: qi::LogContextAttr
.. .. cpp:autoenum:: qi::LogLevel

.. cpp:autofunction:: qi::log::addCategory(const std::string&)
.. cpp:autofunction:: qi::log::addFilter(const std::string&, qi::LogLevel, SubscriberId)
.. cpp:autofunction:: qi::log::addFilters(const std::string&, SubscriberId)
.. cpp:autofunction:: qi::log::addLogHandler(const std::string&, qi::log::logFuncHandler, qi::LogLevel)

.. cpp:autofunction:: qi::log::categories()
.. cpp:autofunction:: qi::log::color()
.. cpp:autofunction:: qi::log::context()

.. cpp:autofunction:: qi::log::destroy()
.. cpp:autofunction:: qi::log::disableCategory(const std::string&, SubscriberId)

.. cpp:autofunction:: qi::log::enableCategory(const std::string&, SubscriberId)

.. cpp:autofunction:: qi::log::flush()

.. cpp:autofunction:: qi::log::init(qi::LogLevel, qi::LogContext, bool)
.. cpp:autofunction:: qi::log::isVisible(CategoryType, qi::LogLevel)
.. cpp:autofunction:: qi::log::isVisible(const std::string&, qi::LogLevel)

.. cpp:autofunction:: qi::log::log(const qi::LogLevel, CategoryType, const std::string&, const char*, const char*, const int)
.. cpp:autofunction:: qi::log::log(const qi::LogLevel, const char*, const char*, const char*, const char*, const int)
.. cpp:autofunction:: qi::log::logLevel(SubscriberId)
.. cpp:autofunction:: qi::log::logLevelToString(const qi::LogLevel, bool)

.. cpp:autofunction:: qi::log::removeLogHandler(const std::string&)

.. cpp:autofunction:: qi::log::setColor(LogColor)
.. cpp:autofunction:: qi::log::setContext(int)
.. cpp:autofunction:: qi::log::setSynchronousLog(bool)
.. cpp:autofunction:: qi::log::setLogLevel(const qi::LogLevel, SubscriberId)
.. cpp:autofunction:: qi::log::stringToLogLevel(const char*)


Deprecated
==========

.. cpp:autofunction:: qi::log::setVerbosity(const qi::LogLevel, SubscriberId)
.. cpp:autofunction:: qi::log::setVerbosity(const std::string&, SubscriberId)
.. cpp:autofunction:: qi::log::setVerbosity(SubscriberId, const qi::log::LogLevel)
.. cpp:autofunction:: qi::log::setCategory(const std::string&, qi::LogLevel, SubscriberId)
.. cpp:autofunction:: qi::log::setCategory(SubscriberId, const std::string&, qi::log::LogLevel)
.. cpp:autofunction:: qi::log::verbosity(SubscriberId)
