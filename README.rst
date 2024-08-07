DISCONTINUATION OF PROJECT

This project will no longer be maintained by Intel.  
Intel has ceased development and contributions including, but not limited to, maintenance, bug fixes, new releases, or updates, to this project.  
Intel no longer accepts patches to this project.  
If you have an ongoing need to use this project, are interested in independently developing it, or would like to maintain patches for the open source software community, please create your own fork of this project.  

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

  - https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html

- pip help for installing from git repos

  - https://pip.pypa.io/en/stable/cli/pip_install/#examples
  
  - https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#direct-url-dependencies
  
    - **"PyPI and other standards-conformant package indices do not accept packages that declare dependencies using direct URLs. pip will accept them when installing packages from the local filesystem or from another URL, however."**

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
