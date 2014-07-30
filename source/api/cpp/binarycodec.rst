.. _api-binarycodec:
.. cpp:namespace:: qi
.. cpp:auto_template:: True
.. default-role:: cpp:guess

Binary Codec
************

Summary
-------

.. cpp:brief::


Reference
---------

.. cpp:autofunction:: qi::encodeBinary(qi::Buffer *buf, const AutoAnyReference &gvp, SerializeObjectCallback onObject=SerializeObjectCallback(), StreamContext* ctx=0)

.. cpp:autofunction:: qi::decodeBinary(qi::BufferReader *buf, AnyReference gvp, DeserializeObjectCallback onObject=DeserializeObjectCallback(), StreamContext* ctx = 0)
