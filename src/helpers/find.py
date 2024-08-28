import os

def traverse_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def find_files_for_hashing(directory, original_files):
    files = traverse_directory(directory)
    modded_files = []
    for file in files:
        relative_file = os.path.relpath(file, directory)
        if relative_file not in original_files:
            modded_files.append(file)
    return modded_files
