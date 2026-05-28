"""
Scan project data folders for duplicate files (by content hash) and optionally move duplicates
into `app/data/duplicates/` for manual review.

Usage:
    python tools/deduplicate_data.py --report
    python tools/deduplicate_data.py --move

This script is safe by default (report mode). Move mode will relocate duplicates (not delete).
"""
import hashlib
import os
import shutil
import argparse
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CANDIDATE_DIRS = [
    os.path.join(ROOT, 'app', 'data'),
    os.path.join(ROOT, 'data'),
    os.path.join(ROOT, 'v0Archive'),
]

IGNORED_DIRS = set(['node_modules', '__pycache__'])


def file_hash(path, chunk_size=8192):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()


def gather_files():
    files = []
    for base in CANDIDATE_DIRS:
        if not os.path.exists(base):
            continue
        for root, dirs, filenames in os.walk(base):
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
            for name in filenames:
                if name.startswith('.'):
                    continue
                path = os.path.join(root, name)
                files.append(path)
    return files


def find_duplicates(files):
    hash_map = defaultdict(list)
    for p in files:
        try:
            h = file_hash(p)
            hash_map[h].append(p)
        except Exception as e:
            print(f"Skipping {p}: {e}")
    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    return duplicates


def report(duplicates):
    if not duplicates:
        print('No duplicate files found.')
        return
    print('Duplicate files found:')
    for h, paths in duplicates.items():
        print('\n----')
        for p in paths:
            print(p)


def move_duplicates(duplicates, target_dir=None):
    if not duplicates:
        print('No duplicates to move.')
        return
    if target_dir is None:
        target_dir = os.path.join(ROOT, 'app', 'data', 'duplicates')
    os.makedirs(target_dir, exist_ok=True)
    for h, paths in duplicates.items():
        # keep the first path as canonical, move others
        canonical = paths[0]
        for dup in paths[1:]:
            rel = os.path.relpath(dup, ROOT)
            dest = os.path.join(target_dir, rel.replace(os.sep, '_'))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            try:
                shutil.move(dup, dest)
                print(f"Moved duplicate {dup} -> {dest}")
            except Exception as e:
                print(f"Failed to move {dup}: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find and optionally move duplicate data files')
    parser.add_argument('--report', action='store_true', help='Only report duplicates')
    parser.add_argument('--move', action='store_true', help='Move duplicates to app/data/duplicates')
    args = parser.parse_args()

    files = gather_files()
    duplicates = find_duplicates(files)
    report(duplicates)
    if args.move:
        move_duplicates(duplicates)
    else:
        print('\nRun with --move to relocate duplicates into app/data/duplicates for review.')
