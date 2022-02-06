#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juptyer Development Team.
# Distributed under the terms of the Modified BSD License.

#-----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython/Jupyterhub)
#-----------------------------------------------------------------------------

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
    name                = 'finailab_install',
    packages            = ['finailab_install'],
    version             = version_ns['__version__'],
    description         = """REMOTE_USER Authenticator: An Authenticator for Jupyterhub to read user information from HTTP request headers, as when running behind an authenticating proxy.""",
    long_description    = "",
    author              = "Carl (https://github.com/cwaldbieser)",
    author_email        = "tatsat@gmail.com",
    url                 = "https://github.com/tatsath/finailab_install",
    license             = "GPLv3",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    data_files          = [('.', ['version.py'])],
)

# setuptools requirements
if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires = []
    install_requires.append('jupyterlab')

def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
