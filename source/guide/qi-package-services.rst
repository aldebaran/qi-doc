.. _guide-qi-package-services:

Packaging services in an application
====================================

In this guide, we will see how to automatically register objects in the service directory.
For this we will package python or C++ services in an application that can be deployed on a robot.

.. warning::

  At the time of writing, packaging of services in an application is not possible in choregraphe,
  and some information could be lost if you open the application using it.

  For the moment, you need some manual operations to package and transfer your application.

Preparing the package for a python service
------------------------------------------

First, write a python file that defines a class corresponding to your service,
instantiate an object, and :ref:`register it using a session<guide-py-service>`.

For the sake of this example, we will reuse the MyFooService object.
Registration of this object is done in a register_foo_service.py file.

Once this script is written, import it in a choregraphe project, or write a .pml
and a manifest.xml yourself:

.. code-block:: xml

    <!-- in foo/foo.pml -->
    <Package>
      <qipython name="foo" />
    </Package>

    <!-- in foo/qiproject.xml -->
    <project version="3">
      <qipython name="foo">
        <script src="register_foo_service.py" />
      </qipython>
    </project>

You will then need to manually edit the manifest of the application in order to specify
your script needs to be handled by the service manager.

Edit your behavior manifest and add a 'services' section.


.. code-block:: xml

  <!-- in foo/manifest.xml -->
  <Package uuid="foo" version="0.1">
    <services>
      <service name="foo_service" autorun="true" execStart="python2 bin/register_foo_service.py" />
    </services>
  </Package>

**name** will be used to :ref:`interact with the service manager<manage_service_registration>` from any part of naoqi.

Set **autorun** to true for the script to be automatically executed when naoqi starts.

**execStart** contains the command to execute in order to launch the script.


You can now package your application and transfer it to the robot, using either Choregraphe or ``qipkg``:

.. code-block:: console

  qipkg make-package foo/foo.pml
  qipkg deploy-package foo-0.1.pkg


Preparing the package for a C++ service
---------------------------------------

.. warning::

   Compilation of C++ applications implies that you need to use the proper toolchains
   for the module to function on a given environment.

   Here, we will concentrate on a c++ application compiled to run on Nao.


First, create a :ref:`C++ qi application that registers a C++ service<guide-cxx-service>`.

You will then compile it using the appropriate flags.

.. code-block:: console

  qibuild configure -c your-atom-cross-toolchain -p nao --release yourproject

Import the executable in a choregraphe application, or create a ``yourproject.pml`` file:

.. code-block:: xml

  <!-- in yourproject/yourproject.pml -->
  <Package>
    <qibuild name="yourproject" />
  </Package>

  <!-- in yourproject/qiproject.xml -->
  <project version="3">
    <qibuild name="yourproject" />
  </project>

Then, you will need to edit your manifest to specify that this executable can be launched by
the service manager.

Edit your behavior manifest and add a 'services' section.
In this precise case, we also need our executable to have execution rights.
This can be specified in the manifest using an *executableFiles* tag.

For the sake of this example, we will use a *my_service* executable.

.. code-block:: xml

  <Package uuid="my_package" version="0.1">
    ...
    <executableFiles>
      <file path="bin/my_service" />
    </executableFiles>

    <services>
      <service name="my_cpp_service" autorun="true" execStart="./bin/my_service" />
    </services>
    ...
  </Package>


Packaging and installing the service
------------------------------------

Run ``qipkg make-package /path/to/pml`` to generate the binary package:

.. code-block:: console

  cd foo_service_app
  qipkg make-package foo.pml

Then, you can transfer it on the robot by an external mean. Here we will use scp

.. code-block:: console

  qipkg deploy-package foo.pkg --url nao@myRobotIp

If you want to remove the package, you can use the following command with the application uuid.

.. code-block:: console

  qicli call PackageManager.removePkg foo_service_app-4da232

.. _manage_service_registration:

Manage service registration
---------------------------

You can execute operations on the services registered with a manifest
by using the Service Manager.

To stop a running service:

.. code-block:: console

  qicli call ALServiceManager.stopService foo_service

To start a service that was registered but is not running at the moment.

.. code-block:: console

  qicli call ALServiceManager.startService foo_service


Troubleshooting
---------------

Here is a list of a few problems you might encounter following this page.

Problem 1
.........

You copied a pkg on your robot and get:

.. code-block:: console

  qicli call PackageManager.install test_cpp_service.pkg
  PackageManager.install: ERROR: test_cpp_service.pkg: no such file

**Probable cause**

You need to use the absolute path of your package when installing.
Make sure to use

.. code-block:: console

  qicli call PackageManager.install /home/nao/test_cpp_service.pkg


Problem 2
.........

You copied a pkg on your robot and get:

.. code-block:: console

  qicli call PackageManager.install /home/nao/test_cpp_service.pkg
  PackageManager.install: ERROR: error while trying to find manifest.xml in project archive /home/nao/test_cpp_service.pkg: (Empty error message)

**Probable cause**


You created your package by zipping the folder containing your files instead of the files directly.
The manifest must be at the root of the package.

Problem 3
.........

You get a warning when your service is supposed to start

.. code-block:: console

  [W] 16967 core.processmanager.qt: my_cpp_service: service failed to start (Permission denied)

**Probable cause**


You did not set your file as an executable file. So it does not have the rights to be launched.
Make sure to use the *executableFiles* tag.
