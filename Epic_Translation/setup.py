#!/usr/bin/env python3

import setuptools
import os
import glob

with open("REAME.md", "r") as readme:
    description = readme.read()

setuptools.setup(
    name='Epic_Translation',
    version='0.0.1',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob('src/*.py')],
    long_description=description,
    install_requires=["nltk"],
)
