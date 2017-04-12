# !usr/bin/python
# -*- coding: utf-8 -*-
# /test.py

import unittest
import coverage
import os

COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'tests/*',
        'app/config.py',
        'venv/*'
    ]
)
COV.start()
tests = unittest.TestLoader().discover('tests')
result = unittest.TextTestRunner(verbosity=2).run(tests)
if result.wasSuccessful():
    COV.stop()
    COV.save()
    print('Coverage Summary:')
    COV.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    COV.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    COV.erase()