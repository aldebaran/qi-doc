.. _api-signature:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

qi::Signature
*************

Summary
-------

.. cpp:brief::


Reference
---------

.. cpp:autoclass:: qi::Signature
.. cpp:autofunction:: signatureSplit


.. cpp:autofunction:: makeTupleSignature(const std::vector<qi::AnyReference>& vgv, bool resolveDynamic = false, const std::string &name = std::string(), const std::vector<std::string>& names)
.. cpp:autofunction:: makeTupleSignature(const std::vector<TypeInterface*>& vgv, const std::string &name = std::string(), const std::vector<std::string>& names)
.. cpp:autofunction:: makeTupleSignature(const qi::Signature& element)
.. cpp:autofunction:: makeListSignature
.. cpp:autofunction:: makeVarArgsSignature
.. cpp:autofunction:: makeKwArgsSignature
.. cpp:autofunction:: makeMapSignature
