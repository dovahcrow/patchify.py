#!/usr/bin/env python3
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# # Get the long description from the README file
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='patchify',
    version='0.0.1',
    description='',
    long_description="An attempt on model interpretation",
    url='https://github.com/doomsplayer/patchify.py',
    author='Weiyüen Wu',
    author_email='doomsplayer@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics :: Editors',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords=['patch', 'image', 'split'],
    py_modules=["patchify"],
    install_requires=["itertools", "numpy", "scikit-image"],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
