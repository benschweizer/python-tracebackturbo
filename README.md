tracebackturbo
==============
A drop-in replacement for the python2 [traceback module](http://docs.python.org/library/traceback.html)
that dumps the local variable scope aside normal stack traces.

Usage
-----
```python
import tracebackturbo as traceback

def erroneous_function():
    ham = u"unicode string with umlauts äöü."
    eggs = "binary string with umlauts äöü."
    i = 23
    if i>5:
        raise Exception("it's a trap!")

try:
    erroneous_function()
except:
    print traceback.format_exc(with_vars=True)
```

Sample Output
-------------
This is the output of tracebackturbo:
```
Traceback Turbo (most recent call last):
  File "test.py", line 11, in 
    Local variables:
      __builtins__ = 
      __doc__ = None
      __file__ = "x"
      __name__ = "__main__"
      __package__ = None
      erroneous_function = 
      traceback = <module 'tracebackturbo' from '/private/tmp/python-...
    erroneous_function()
  File "test.py", line 8, in erroneous_function
    Local variables:
      eggs = "binary string with umlauts \xc3\xa4\xc3\xb6\xc3\xbc."
      ham = u"unicode string with umlauts ???."
      i = 23
    raise Exception("it's a trap!")
Exception: it's a trap!
```

versus the normal output:
```
Traceback Turbo (most recent call last):
  File "test.py", line 11, in 
    erroneous_function()
  File "test.py", line 8, in erroneous_function
    raise Exception("it's a trap!")
Exception: it's a trap!
```

Setup
-----
To setup tracebackturbo, simply drop the script in your working directory or
install the egg from pypi:
```
$ pip install tracebackturbo
```

Python3
-------
Since python3.5, there's a new TracebackException class that implements
similar functionality, see [https://bugs.python.org/issue17911](https://bugs.python.org/issue17911).
Since the control variable capture_local is not yet published as of of python3.6, 
you can use this patched version: https://github.com/cxcv/python-tracebackturbo3

License & Credit
-----------------
This code is based upon the original traceback module that ships with stock
python. This modules used the [Python License](http://www.opensource.org/licenses/Python-2.0).
