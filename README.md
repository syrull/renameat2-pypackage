# rename_exchange

This is a python package for the `renameat2` and `RENAME_EXCHANGE` to do to do atomic (directory) replacement.

---
**NOTE**

This is a package created specifically for asottile's puzzels (02). It is not meant to be
used in any kind of production env.

---

# Build

## Building with abi3 wheel

```console
$ python setup.py bdist_wheel --abi3
```
The default build can be run without the `--abi3`.

## Building the manylinux wheels

The script will generate a `wheelhouse` storing all the wheels. You need docker to use this script.

You can change the `PLAT` env variable to the ones specified here https://github.com/pypa/manylinux

```console
$ docker run --rm -e PLAT=manylinux1_x86_64 -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64 bash /io/build-wheels.sh
```

The script will execute the `build-wheels.sh` which will generate the wheels and test them against 
our `test.py`.

# Testing

```console
$ virutalenv venv && . ./venv/bin/activate
$ pip install -r dev-requirements.txt && pip install .
$ pytest test.py
```
