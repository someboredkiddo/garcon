from setuptools import find_packages
from setuptools import setup
from codecs import open
from os import path

from garcon import __version__


here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='owsgarcon',
    version=__version__,
    url='https://github.com/theorchard/garcon/',
    author='The Orchard',
    author_email='webdev@theorchard.com',
    description=(
        'Orchard Fork of Lightweight library for AWS SWF.'),
    long_description=long_description,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['boto', 'backoff'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],)
