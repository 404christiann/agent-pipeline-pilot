import pytest

from sample import item_count


def test_empty_list_has_zero_items():
    assert item_count([]) == 0


def test_single_item_list():
    assert item_count(["a"]) == 1


def test_multi_item_list():
    assert item_count(["a", "b", "c"]) == 3


def test_none_is_rejected_rather_than_counted():
    with pytest.raises(TypeError):
        item_count(None)
