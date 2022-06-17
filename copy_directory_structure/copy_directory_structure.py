import argparse
import os
from pathlib import Path


def copy_directory_structure(source: Path, destination: Path):

    if not source.is_dir():
        raise ValueError('source expects a folder location')
    if not destination.is_dir():
        raise ValueError('destination expects a folder location')

    if os.listdir(destination) != 0:
        raise ValueError('The destination folder is not empty')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process two strings')
    parser.add_argument('source', type=Path, help='copy folder structure from this directory')
    parser.add_argument('destination', type=Path, help='copy the folder structure in this folder')

    args = parser.parse_args()

    copy_directory_structure(args.source, args.destination)

