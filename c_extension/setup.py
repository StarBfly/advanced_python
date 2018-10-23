from distutils.core import Extension
from distutils.core import setup

py_ext = Extension("fib",
                   define_macros=[('MAJOR_VERSION', '1'),
                                  ('MINOR_VERSION', '0')],
                   sources=['fibonacci.c'])

setup(name="Hello Package",
      version='1.0',
      ext_modules=[py_ext])
