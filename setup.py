# this is your project's setup.py script

import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

from setuptools import setup

class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')


setup(
  name = 'zosapi',
  packages = ['zosapi'], # this must be the same as the name above
  version = '0.2',
  description = 'A class to connect to Zemax OpticStudio API via .NET',
  long_description = 'A  class to connet to Zemax OpticStudio API via .NET',
  author = 'Michael Humphreys',
  author_email = 'michael.humphreys@zemax.com',
  url = 'https://github.com/x68507/zosapi',
  download_url = 'https://github.com/x68507/zosapi/tarball/0.1',
  keywords = ['zosapi', 'zemax', 'opticstudio'], 
  classifiers = [],
  cmdclass={
    'register': register,
    'upload': upload
  },
  install_requires=[
    'pythonnet',
    'matplotlib'
  ]
)