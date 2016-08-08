#!/usr/bin/env python

from setuptools import setup


VERSION = "0.1"
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
]


if __name__ == '__main__':
    setup(
        name = "map_mpi",
        author = "Hai Nguyen",
        author_email = "hainm.comp@gmail.com",
        description = "Ready to use simple mpi",
        version = VERSION,
        classifiers = CLASSIFIERS,
        license = "MIT",
        url = "https://github.com/hainm/map_mpi",
        zip_safe = False,
        packages = [ "map_mpi"],
        install_requires = ["mpi4py", "numpy"],
    )
