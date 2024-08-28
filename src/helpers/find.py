import os
from src.helpers.attributes import generate_file_hash

def traverse_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def find_files_for_hashing(directory, original_hashes):
    files = traverse_directory(directory)
    modded_files = []
    for file in files:
        file_hash = generate_file_hash(file)
        if file_hash not in original_hashes:
            modded_files.append(file)
    return modded_files
