#!/usr/bin/env python

import sys
import os
from distutils.core import setup

setup(name='flaskle',
      version='0.1.2a',
      description='bottle-like utility decorators for flask',
      #long_description='tl;dr;',
      author='Anderson Pierre Cardoso',
      author_email='apierre.cardoso@gmail.com',
      # url='',
      py_modules=['flaskle'],
      scripts=['flaskle.py'],
      install_requires=['flask'],
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
