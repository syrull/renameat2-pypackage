import platform
import sys

from setuptools import Extension, setup

if platform.python_implementation() == "CPython":
    try:
        import wheel.bdist_wheel
    except ImportError:
        cmdclass = {}
    else:

        class bdist_wheel(wheel.bdist_wheel.bdist_wheel):
            def finalize_options(self):
                self.py_limited_api = "cp3{}".format(sys.version_info[1])
                super().finalize_options()

        cmdclass = {"bdist_wheel": bdist_wheel}

setup(
    name="renameat",
    version="1.0",
    description="This is a package for asottile's puzzle 02",
    packages=["renameat"],
    ext_modules=[
        Extension(
            "_renameat",
            sources=["_renameat.c"],
            define_macros=[("Py_LIMITED_API", None)],
            py_limited_api=True,
        )
    ],
    cmdclass=cmdclass,
)
