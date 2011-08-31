tracebackturbo
==============
This is an improved Python [traceback module][http://docs.python.org/library/traceback.html]
which logs variables from the local scope next to the affected code.

Usage
-----
``` python
import tracebackturbo as traceback

def erroneous_function():
    ham = u"unicode string with umlauts äöü."
    eggs = "binary string with umlauts äöü."
    i = 23
    if i>5:
        raise Exception("it's true!")

try:
    erroneous_function()
except:
    print traceback.format_exc(with_vars=True)
```

Sample Output
-------------
```
Traceback (most recent call last):
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
    raise Exception("it's true!")
Exception: it's true!
```

Links
-----
http://benjamin-schweizer.de/improved-python-traceback-module.html
