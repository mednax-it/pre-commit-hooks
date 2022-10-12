from __future__ import annotations

import argparse
import os
import re
from typing import Sequence

def _has_primary_and_secondary(filename: str) -> bool:
    has_primary=False
    has_secondary=False
    with open(filename) as file_processed:
        for line in file_processed:
            if re.search(r'Primary\s*=\s*true', line, re.IGNORECASE):
                has_primary = True
            if re.search(r'Primary\s*=\s*false', line, re.IGNORECASE):
                has_secondary = True

    return has_primary == has_secondary

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    return_code = 0

    print(args.filenames)

    for filename in args.filenames:
        if filename.endswith(".tf"):
            if not _has_primary_and_secondary(filename): 
                print(f'Error in {filename}')
                return_code = 1

    return return_code

if __name__ == '__main__':
    raise SystemExit(main())
