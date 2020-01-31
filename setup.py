import os
import sys
import pathlib
from setuptools import setup

ORG = "intel"
NAME = "project-example-for-python"
DESCRIPTION = "A short desciption of your project"
VERSION = "1.33.7"
AUTHOR_NAME = "You Name Here!"
AUTHOR_EMAIL = "some.body@once.toldme"

SELF_PATH = os.path.dirname(os.path.abspath(__file__))

README = pathlib.Path(SELF_PATH, "README.md").read_text()

# Folders on disk for Python packages must be _ and not -
IMPORT_NAME = NAME.replace("-", "_")

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    # long_description_content_type is needed to make non-rst readmes display
    # correctly in PyPi, if you see a warning saying something like "I don't
    # know what this means" don't listen to it, it lies, it does know what this
    # means and if you have a .md README then you need to keep this line.
    long_description_content_type="text/markdown",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url='https://github.com/{}/{}'.format(ORG, NAME),
    license='MIT',

    keywords=[
        'this',
        'is',
        'where',
        'searchable',
        'keywords',
        'go',
    ],

    # Your package will fail to upload if you don't abide by these dude!:
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        # You must list all the version of Python that you want to allow to
        # download your package here. If you don't list it, users trying to pip
        # install it won't be able to get it from PyPi
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    # Dependencies got here aka install_requires=['dffml']
    install_requires=[],
    # Dependencies only needed for running your tests go here
    tests_require=[],
    # If you include data files in your repo, you probably want the following
    # two lines
    include_package_data=True,
    zip_safe=False,
    # Install development dependencies with
    # pip install folder_containing_this_setup_py[dev]
    extras_require={
        "dev": [
            "coverage",
            "codecov",
            "sphinx",
            "sphinxcontrib-asyncio",
            "black",
            "sphinx_rtd_theme",
        ],
    },
    # Python's plugin system, console_scripts says make command line utilities
    # out of these functions, note the `python.path : obj_in_file` syntax.
    # Don't forget the `:`!
    entry_points={
        'console_scripts': [
            'script = {}.cli:SCRIPT'.format(IMPORT_NAME),
            'scriptscript = {}.cli_again:SCRIPTSCRIPT'.format(IMPORT_NAME),
            'ufb = {}.cli:import_SCRIPT'.format(IMPORT_NAME),
        ],
    },
)
