#!/usr/bin/env python
from distutils.core import setup

setup(name='flaskle',
      version='0.4',
      description='bottle-like utility decorators for flask',
      #long_description='tl;dr;',
      author='Anderson Pierre Cardoso',
      author_email='apierre.cardoso@gmail.com',
      # url='',
      py_modules=['flaskle'],
      scripts=['flaskle.py'],
      install_requires=['Flask'],
      license='MIT',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ]
)
