import os
from pathlib import Path

import pytest

from copy_directory_structure.copy_directory_structure import copy_directory_structure, copy_level, get_subfolder_names


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


def test_destination_is_not_empty(nested_source: Path, empty_destination: Path) -> None:
    (empty_destination / 'some_folder').mkdir(parents=True)

    assert len(os.listdir(empty_destination)) == 1

    with pytest.raises(ValueError) as e:
        copy_directory_structure(nested_source, empty_destination)
        assert 'not empty' in e.value


def test_copy_level(nested_source: Path, empty_destination: Path) -> None:
    source_folders = get_subfolder_names(nested_source)
    destination_folders = get_subfolder_names(empty_destination)
    assert len(source_folders) != len(destination_folders)

    copy_level(nested_source, empty_destination)

    source_folders = get_subfolder_names(nested_source)
    destination_folders = get_subfolder_names(empty_destination)
    assert len(source_folders) == len(destination_folders)


def test_files_not_copied(nested_source: Path, empty_destination: Path) -> None:

    # Get total number of files in the nested source
    num_files = 0
    for _, _, files in os.walk(nested_source):
        num_files += len(files)
    # Assert there are more than 0 files in the source
    assert num_files > 0

    # Populate destination
    copy_level(nested_source, empty_destination)

    # Get total number of files in the populated destination
    num_files = 0
    for _, _, files in os.walk(empty_destination):
        num_files += len(files)
    # Assert no files have been copied
    assert num_files == 0





