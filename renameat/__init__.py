import typing
from pathlib import PosixPath

import _renameat


def rename_exchange(
    path1: typing.Union[str, PosixPath], path2: typing.Union[str, PosixPath]
) -> None:
    if isinstance(path1, PosixPath):
        _path1 = str(path1.absolute())
    else:
        _path1 = path1
    if isinstance(path2, PosixPath):
        _path2 = str(path2.absolute())
    else:
        _path2 = path2
    _renameat.rename_exchange(_path1, _path2)
