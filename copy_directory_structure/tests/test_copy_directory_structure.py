import os
from pathlib import Path

import pytest

from copy_directory_structure.copy_directory_structure import copy_directory_structure


def test_source_is_folder():
    source = Path('test/nest/file.py')
    destination = Path('/some_directory/')
    with pytest.raises(ValueError) as e:
        copy_directory_structure(source, destination)
        assert 'source' in e.value


def test_destination_is_folder():
    source = Path('/some_directory/')
    destination = Path('test/nest/file.py')
    with pytest.raises(ValueError) as e:
        copy_directory_structure(source, destination)
        assert 'destination' in e.value


def test_destination_is_not_empty(nested_source, empty_destination):
    (empty_destination / 'some_folder').mkdir(parents=True)

    assert len(os.listdir(empty_destination)) == 1

    with pytest.raises(ValueError) as e:
        copy_directory_structure(nested_source, empty_destination)
        assert 'not empty' in e.value




