#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juptyer Development Team.
# Distributed under the terms of the Modified BSD License.

# -----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython/Jupyterhub)
# -----------------------------------------------------------------------------

from __future__ import print_function

import os
import sys

from setuptools import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version.
version_ns = {}
with open(pjoin(here, 'version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = dict(
    name='quanturf',
    packages=['quanturf'],
    version="7.3",
    description="""REMOTE_USER Authenticator: An Authenticator for Jupyterhub to read user information from HTTP request headers, as when running behind an authenticating proxy.""",
    long_description="",
    author="Carl (https://github.com/tatsath)",
    author_email="tatsatx@gmail.com",
    url="https://github.com/tatsath/finailab",
    license="GPLv3",
    platforms="Linux, Mac OS X",
    keywords=['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    package_data={'': ['quanturf.ipynb']},
    include_package_data=True,
    data_files=[('.', ['version.py'])],
    # scripts=['bin/run_quanturf'],
    entry_points={
        "console_scripts": [
            "myscript = quanturf.__main__:main",
        ]
    }
)

# setuptools requirements
if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires = []
    install_requires.append('jupyterlab')
    install_requires.append('jupyterlab_templates')


def main():
    setup(**setup_args)


if __name__ == '__main__':
    main()
