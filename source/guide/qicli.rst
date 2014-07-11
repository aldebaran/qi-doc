
.. cpp:auto_template:: True

.. default-role:: cpp:guess

.. _guide-qicli:

How to use qicli
*****************

Introduction
============

This guide will show you how to use qicli commands in order to see information, use methods and watch signals.

Prerequisite
------------

- Make sure **NAOqi** is running

how to run qicli
----------------

- Connect on SSH to you robot.
- Use qicli on your computer and connect remotely on a robot.

.. code-block:: bash

$ ./qicli cmd args --qi-url IPofYourRobot

qicli info
----------

qicli info is used to display:
- a list of services and
- a detailed list of methods and signals of specific services.

With no argument, it lists services:

.. code-block:: bash

   $ qicli info
   > 001 [ServiceDirectory]
     002 [LogManager]
     003 [ALFileManager]
     004 [ALMemory]
     005 [ALLogger]
     ...

This is equivalent to:

.. code-block:: bash

   $ qicli info --list
   $ qicli info -l
   $ qicli # Without any argument


With a service's name as argument, it gives:

.. code-block:: bash

   $ qicli info ServiceDirectory
   > 001 [ServiceDirectory]
     * Info:
      machine   37814cee-e5a8-4183-9862-65d10460f0e5
      process   3665
      endpoints tcp://127.0.0.1:9559
                tcp://198.18.0.1:9559
                tcp://10.2.1.177:9559
     * Methods:
      100 service            (String)
      101 services          List<> ()
      102 registerService   UInt32 ()
      103 unregisterService Void (UInt32)
      104 serviceReady      Void (UInt32)
      105 updateServiceInfo Void ()
      108 machineId         String ()
     * Signals:
      106 serviceAdded   (UInt32,String)
      107 serviceRemoved (UInt32,String)

There is always 3 parts:

**Info**
  general information about service,
**Methods**
  list of methods,
**Signals**
  list of signals.

The 2 last parts may be empty.

**Methods** and **Signal** follow the format::

   [id] name    [return_type] ([parameters_types...])

If the name of the service is a bit long, identifiers can be used instead:

.. code-block:: bash

   $ qicli info ServiceDirectory
   $ qicli info 1

Command also accept several services' names simultaneously:

.. code-block:: bash

   $ qicli info ServiceDirectory LogManager
   > 001 [ServiceDirectory]
       * Info:
        machine   37814cee-e5a8-4183-9862-65d10460f0e5
        process   3665
        endpoints tcp://127.0.0.1:9559
                  tcp://198.18.0.1:9559
                  tcp://10.2.1.177:9559
       * Methods:
        100 service            (String)
        101 services          List<> ()
        102 registerService   UInt32 ()
        103 unregisterService Void (UInt32)
        104 serviceReady      Void (UInt32)
        105 updateServiceInfo Void ()
        108 machineId         String ()
       * Signals:
        106 serviceAdded   (UInt32,String)
        107 serviceRemoved (UInt32,String)
     002 [LogManager]
       * Info:
        machine   37814cee-e5a8-4183-9862-65d10460f0e5
        process   3665
        endpoints tcp://127.0.0.1:9559
                  tcp://198.18.0.1:9559
                  tcp://10.2.1.177:9559
       * Methods:
        100 log            Void (LogMessage)
        101 getListener    Object ()
        102 addProvider    Int32 (Ob ject)
        103 removeProvider Void (Int32)
       * Signals:

Globing can also be used:

.. code-block:: bash

   $ qicli info "LogMa*"
   > 002 [LogManager]
       * Info:
        machine   37814cee-e5a8-4183-9862-65d10460f0e5
        process   3665
        endpoints tcp://127.0.0.1:9559
                  tcp://198.18.0.1:9559
                  tcp://10.2.1.177:9559
       * Methods:
        100 log            Void (LogMessage)
        101 getListener    Object ()
        102 addProvider    Int32 (Object)
        103 removeProvider Void (Int32)
       * Signals:

Advanced features
+++++++++++++++++

- Extra options:

**--show-doc**
  show documentation for methods, signals and properties.

**--hidden**
  show hidden services, methods, signals and properties.

**--raw-signature**
  show the raw signature.

**-z**
  prints the result in a parseable format

- Logging options:

./doc/general/source/dev/tools/naoqi-man.rst

qicli call
----------

This command allows you to call service's methods ans signals.

Returned values follow `json format <http://www.json.org/>`_.

.. code-block:: bash

   $ qicli call ALFileManager.ping
   > ALFileManager.ping: true

More complex return values can also be returned.

.. code-block:: bash

   $ qicli call ALMemory.getEventList
   > ALMemory.getEventList: [ "/Preferences", "ALAnimatedSpeech/EndOfAnimatedSpeech", "ALAudioSourceLocalization/SoundLocated", "ALAudioSourceLocalization/SoundsLocated", ...]

**Where**

   [ ... ] is a list in json.

Identifiers can also be used instead of names:

.. code-block:: bash

   $ qicli call 4.123
   > ALMemory.getEventList: [ "/Preferences", "ALAnimatedSpeech/EndOfAnimatedSpeech", "ALAudioSourceLocalization/SoundLocated", "ALAudioSourceLocalization/SoundsLocated", ...]

Several arguments can be given:

.. code-block:: bash

   $ qicli call ServiceDirectory.service PackageManager
   > ServiceDirectory.service: [ "PackageManager", 41, "4fd62363-f74d-4c6d-81d1-c1b9304c77d2", 3840, [ "tcp://10.0.252.216:34510", "tcp://127.0.0.1:34510" ], "0967f415-db38-43a4-b5a9-7ac70539891d" ]

Complex arguments (list, objects) of methods must be given in JSON with option
**--json**.

.. warning::

   JSON and terminals do not work well together.

.. code-block:: bash

   $ qicli call --json ALMemory.insertListData "[[\"foo\",true],[\"bar\",1]]"
   > ALMemory.insertListData: null

In order to call a hidden method, add **--hidden**

- Extra options:

**--method arg**
  method's name
**--arg arg**
  method's args
**--bench arg**
  bench the call time using given iteration count
**--continue**
  continue on error

qicli watch
-----------

Qicli watch is used to see when a signal is triggered.

For example, to get information each time a package is installed on your robot, use:

.. code-block:: cpp

  $ qicli watch PackageManager.onPackageInstalled

- Extra options:

**-s [ --signal ] arg**
  service's name
**-t [ --time ]**
  Print time
**--hidden**
  watch hidden signals if they match the given pattern
**--continue**
  continue on error
**--almemory**
  watch ALMemory events

qicli log-view
--------------

Qicli log-view is used to display logs.

.. code-block:: cpp

  $ qicli log-view

- Extra options:

**-v [ --verbose ]**
  Set maximum logs verbosity shown to verbose.
**-d [ --debug ]**
  Set maximum logs verbosity shown to debug.
**-l [ --level ]**
  arg (=4) Change the log minimum level: [0-6] (default:4). This option accept the same arguments' format than --qi-log-level.
**-f [ --filters ] arg**
  Set log filtering options. This option accepts the same arguments' format than --qi-log-filters.

qicli log-send
--------------

Qicli log-send is used to send logs.

for sending a message:

.. code-block:: cpp

  $ qicli log-send hello

This is equivalent to:

.. code-block:: cpp

  $ qicli log-send --message hello
  $ qicli log-send -m hello

To send a message with your own Message's category (default: "qicli.qilog.logsend"):

.. code-block:: cpp

  $ qicli log-send --category MyCategory -m MyMessage
  $ qicli log-send -c MyCategory -m MyMessage

- Extra options:

**-v [ --verbose ]**
  Set message verbosity to verbose.
**-d [ --debug ]**
  Set message verbosity to debug.
**-l [ --level ] arg (=4)**
  Change the log minimum level: [0-6] (default:4). This option accepts the same arguments' format than --qi-log-level.


