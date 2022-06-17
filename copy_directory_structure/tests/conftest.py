from pathlib import Path

import pytest

@pytest.fixture
def nested_source(tmp_path):

    source = tmp_path / 'source'
    source.mkdir()
    level1 = ['folder_a', 'folder_b', 'folder_c']
    level2 = ['nest_a', 'nest_b']
    for folder in level1:
        for nest in level2:
            path = source / folder / nest
            path.mkdir(parents=True)

    return source

@pytest.fixture
def empty_destination(tmp_path):
    return tmp_path / 'destination'