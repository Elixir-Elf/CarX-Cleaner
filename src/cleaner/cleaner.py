import os
from src.helpers.find import find_files_for_hashing
from src.helpers.attributes import generate_file_hash

def start_cleaning_process(directory):
    original_hashes = {'original_file1_hash', 'original_file2_hash'}
    modded_files = find_files_for_hashing(directory, original_hashes)
    for file in modded_files:
        os.remove(file)

if __name__ == "__main__":
    start_cleaning_process('path_to_carx_directory')
