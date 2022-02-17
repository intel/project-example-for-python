Example Project for Python
##########################

This is an example repo to show you how to create a Python package which can be
published on PiPy. It also includes documentation generation and CI scripts you
can copy.

Install From Git Repo
*********************

.. code-block:: console

    $ pip install -U setuptools pip wheel
    $ pip install "https://github.com/intel/project-example-for-python/archive/refs/heads/master.zip#egg=project-example-for-python"

Usage
*****

.. code-block:: console

    $ export PATH="${HOME}/.local/bin:${PATH}"
    $ script
    SCRIPT!
    $ scriptscript
    SCRIPTSCRIPT!
    $ ufb
    It's a bird it's a plane!
    NO! It's a SCRIPT!!

Contributing
************

See `CONTRIBUTING <CONTRIBUTING.rst>`_

Legal
*****

.. note::

    This software is subject to the U.S. Export Administration Regulations and
    other U.S. law, and may not be exported or re-exported to certain countries
    (Cuba, Iran, Crimea Region of Ukraine, North Korea, Sudan, and Syria) or to
    persons or entities prohibited from receiving U.S. exports (including
    Denied Parties, Specially Designated Nationals, and entities on the Bureau
    of Export Administration Entity List or involved with missile technology or
    nuclear, chemical or biological weapons).
