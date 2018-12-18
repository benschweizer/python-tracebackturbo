# https://packaging.python.org/tutorials/packaging-projects/
import sys
import setuptools

if not '2.6' <= sys.version < '3.0':
    raise ImportError('Python version not supported, consider using tracebackturbo3')

setuptools.setup(name="tracebackturbo",
                 version="0.3",
                 maintainer="Benjamin Schweizer",
                 maintainer_email="cxcv@cxcv.de",
                 description="Patched version of traceback, also dumps local and global scope vars.",
                 classifiers=["Intended Audience :: Developers",
                              "License :: OSI Approved :: Python Software Foundation License",
                              "Programming Language :: Python",
                              "Programming Language :: Python :: 2",
                              "Topic :: Software Development :: Libraries :: Python Modules",
                              ],
                 url="https://github.com/cxcv/python-tracebackturbo",
                 license="PSF",
                 zip_safe=False,
                 packages=setuptools.find_packages(),
                 include_package_data=True
                 )
