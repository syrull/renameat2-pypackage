from pathlib import Path

import pytest

import renameat


def test_rename_exchange(tmp_path):
    f1 = tmp_path / "f1"
    f2 = tmp_path / "f2"
    f1.write_text("a")
    f2.write_text("b")
    renameat.rename_exchange(str(f1), str(f2))
    assert f2.read_text() == "a"
    assert f1.read_text() == "b"


def test_rename_exchange_on_error():
    with pytest.raises(OSError):
        renameat.rename_exchange("not_found", "not_found")


def test_rename_with_pathlib_obj(tmp_path):
    f1 = tmp_path / "f1"
    f2 = tmp_path / "f2"
    f1.write_text("a")
    f2.write_text("b")
    renameat.rename_exchange(f1, f2)
    assert f2.read_text() == "a"
    assert f1.read_text() == "b"
