#!/usr/bin/env python

import sys
import os
from distutils.core import setup
import flaskle

setup(name='flaskle',
      version=flaskle.__version__,
      description='bottle-like utility decorators for flask',
      long_description=flaskle.__doc__,
      author=flaskle.__author__,
      author_email='apierre.cardoso@gmail.com',
      # url='',
      py_modules=['flaskle'],
      scripts=['flaskle.py'],
      license='MIT',
      platforms = 'any',
      classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ]
)