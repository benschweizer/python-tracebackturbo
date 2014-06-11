import sys
from setuptools import setup, find_packages

version = '0.1.2'

if not '2.6' <= sys.version < '3.0':
    raise ImportError('Python version not supported')

setup(name="tracebackturbo",
      version=version,
      maintainer="Benjamin Schweizer",
      maintainer_email="cxcv@cxcv.de",
      description="Patched version of traceback, also dumps local and global scope vars.",
      classifiers=["Intended Audience :: Developers",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      url="https://github.com/cxcv/python-tracebackturbo",
      license="PSF",
      zip_safe=False,
      packages=find_packages(),
      include_package_data=True
      )
