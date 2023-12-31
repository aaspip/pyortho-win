#!/usr/bin/env python
# -*- encoding: utf8 -*-
import glob
import inspect
import io
import os

from setuptools import find_packages
from setuptools import setup


long_description = """
Source code: https://github.com/aaspip/pyortho-win""".strip() 

setup(
    name="pyortho-win",
    version="0.0.1",
    license='GNU General Public License, Version 3 (GPLv3)',
    description="Pyortho-win: A python package for local signal-and-noise orthogonalization and local similarity calculation (windows version)",
    long_description=long_description,
    author="pyortho developing team",
    author_email="chenyk2016@gmail.com",
    url="https://github.com/aaspip/pyortho-win",
    packages=['pyortho'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords=[
        "seismology", "exploration seismology", "array seismology", "denoising", "science", "orthogonalization", "local orthogonalization", "local similarity", "signal-to-noise ratio", "damped rank reduction method"
    ],
    install_requires=[
        "numpy", "scipy", "matplotlib"
    ],
    extras_require={
        "docs": ["sphinx", "ipython", "runipy"]
    }
)
