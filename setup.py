#!/usr/bin/env python
import codecs
import os
import re

from setuptools import find_packages
from setuptools import setup


def meta(category, fpath="src/PACKAGENAME/__init__.py"):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, fpath), "r") as f:
        package_root_file = f.read()
    matched = re.search(
        r"^__{}__\s+=\s+['\"]([^'\"]*)['\"]".format(category), package_root_file, re.M
    )
    if matched:
        return matched.group(1)
    raise Exception("Meta info string for {} undefined".format(category))


requires = []

setup_requires = []

dev_requires = ["flake8", "isort", "pre-commit"]

tests_require = ["pytest"]

setup(
    name="PACKAGENAME",
    version=meta("version"),
    description="PACKAGENAME for Python",
    author=meta("author"),
    url="https://github.com/okomestudio/REPONAME",
    platforms=["Linux"],
    classifiers=[],
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.7",
    scripts=[],
    install_requires=requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require={"dev": dev_requires},
    entry_points={"console_scripts": []},
)
