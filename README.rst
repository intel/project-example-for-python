Example Project for Python
##########################

This is an example repo to show you how to create a Python package which can be
published on PiPy. It also includes documentation generation and CI scripts you
can copy.

Files required to create a Python package (these require find and replacing):

- https://github.com/intel/project-example-for-python/blob/master/pyproject.toml
  - https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
- https://github.com/intel/project-example-for-python/blob/master/setup.cfg
  - https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
  - https://setuptools.pypa.io/en/latest/userguide/distribution.html
  - ``long_description_content_type = "text/markdown"``
    - https://setuptools.pypa.io/en/latest/userguide/declarative_config.html?highlight=long_description#metadata
- https://github.com/intel/project-example-for-python/blob/master/setup.py
- https://github.com/intel/project-example-for-python/blob/master/MANIFEST.in
  -  https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html

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
