#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests del modulo {{ cookiecutter.project_slug }}."""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import unittest
import nose

import {{ cookiecutter.project_slug }}


class {{ cookiecutter.project_slug.replace("_", " ").title().replace(" ", "") }}TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        pass

if __name__ == '__main__':
    nose.run(defaultTest=__name__)
