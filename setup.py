# -*- coding: utf-8 -*-
import os
import re
import sys
from setuptools import setup

from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count
            self.pytest_args = ['-n', str(cpu_count()), '--boxed']
        except (ImportError, NotImplementedError):
            self.pytest_args = ['-n', '1', '--boxed']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


tags = {
        'author': 'Matthew Collie',
        'email': 'mgcollie@gmail.com',
        'version': '1.0.0'
}

install_reqs = []

with open('requirements.txt') as fp:
    content = fp.readlines()
    for line in content:
        item = line.strip('\n')
        install_reqs.append(item)


setup(
        name='mypackage',
        author=tags['author'],
        author_email=tags['email'],
        packages=['mypackage'],
        install_requires=install_reqs,
        version=tags['version'],
        license='Apache License 2.0'
)