import sys
import setuptools
from distutils.core import setup, Extension

if "--abi3" in sys.argv:
    module = Extension(
        "rename_exchange",
        sources=["renameat.c"],
        define_macros=[("Py_LIMITED_API", None)],
        py_limited_api=True,
    )
    sys.argv.remove("--abi3")
else:
    module = Extension(
        "rename_exchange",
        sources=["renameat.c"],
    )

setup(
    name="rename_exchange",
    version="1.0",
    description="This is a package for asottile's puzzle 02",
    ext_modules=[module],
)
