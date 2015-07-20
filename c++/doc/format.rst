Formatting
==========

Example of ``vera++`` rule:

.. literalinclude:: ../src/rules/filenames_lowercase.py

Test it with:

.. code-block:: bash

    vera++ --root src/ -R filenames_lowercase test/Main.cpp
