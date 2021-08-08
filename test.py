import pytest

import rename_exchange

def test_rename_exchange(tmp_path):
    f1 = tmp_path / "f1"
    f2 = tmp_path / "f2"
    f1.write_text("a")
    f2.write_text("b")
    rename_exchange.rename_exchange(f1.__str__(), f2.__str__())
    assert f2.read_text() == "a"
    assert f1.read_text() == "b"

def test_rename_exchange_on_error():
    with pytest.raises(OSError):
        f = rename_exchange.rename_exchange("not_found", "not_found")
        print(f)