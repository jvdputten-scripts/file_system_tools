import argparse
import os
from pathlib import Path
from typing import List


def get_subfolder_names(path: Path) -> List[str]:
    return [f.name for f in os.scandir(path) if f.is_dir()]


def copy_level(source: Path, destination: Path) -> None:
    folders = get_subfolder_names(source)
    while len(folders) > 0:
        folder = folders.pop()
        (destination / folder).mkdir()
        copy_level(source / folder, destination / folder)


def copy_directory_structure(source: Path, destination: Path) -> None:

    # Input validation
    if not source.is_dir():
        raise ValueError('source expects a folder location')
    if not destination.is_dir():
        raise ValueError('destination expects a folder location')

    if len(os.listdir(destination)) != 0:
        raise ValueError('The destination folder is not empty')

    # Start recursion (Top down)
    copy_level(source, destination)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process two strings')
    parser.add_argument('source', type=Path, help='copy folder structure from this directory')
    parser.add_argument('destination', type=Path, help='copy the folder structure in this folder')

    args = parser.parse_args()

    copy_directory_structure(args.source, args.destination)

