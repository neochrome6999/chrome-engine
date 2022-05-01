import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="chrome-engine",
    version="0.0.1",
    author="neochrome6999",
    author_email="flaviusnegulescu0@gmail.com",
    description=("A simple HTML/HTTPS web scraper / crawler library"),
    license="Apache 2.0",
    keywords="web https html scraper crawler",
    url=None,
    packages=None,
    long_description = read('README.md'),
    clasifiers=[
        "Development Status :: 3 - Alpha",
        "Topic: Utilities",
        "License :: OSI Approved :: Apache 2.0"
    ]
)