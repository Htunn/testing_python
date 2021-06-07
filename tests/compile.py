from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("hello", ["hello.py"])
   # all your modules that need be compiles
]

setup(
    name = "Hello",
    cmdclass = {'build_ext', build_ext},
    ext_modules = ext_modules
)