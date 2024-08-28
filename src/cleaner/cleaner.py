import os
import json
from src.helpers.find import find_files_for_hashing

def load_original_hashes(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)

def start_cleaning_process(directory, progress_bar):
    original_hashes = load_original_hashes('src/hashes/relative_hashes.txt')
    original_files = set(original_hashes.keys())
    modded_files = find_files_for_hashing(directory, original_files)
    
    if not modded_files:
        print("No modded files found. The directory is either empty or all files are original.")
        return
    
    total_files = len(modded_files)
    for index, file in enumerate(modded_files):
        relative_file = os.path.relpath(file, directory)
        if relative_file not in original_files:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting file {file}: {e}")
        if progress_bar:
            progress_bar.setValue(int((index + 1) / total_files * 100))
            progress_bar.update()
    
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            relative_dir = os.path.relpath(dir_path, directory)
            if relative_dir not in original_files:
                try:
                    for file in os.listdir(dir_path):
                        file_path = os.path.join(dir_path, file)
                        relative_file_path = os.path.relpath(file_path, directory)
                        if relative_file_path not in original_files:
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                            elif os.path.isdir(file_path) and not os.listdir(file_path):
                                os.rmdir(file_path)
                    if not os.listdir(dir_path):
                        os.rmdir(dir_path)
                except Exception as e:
                    print(f"Error deleting directory {dir_path}: {e}")

if __name__ == "__main__":
    start_cleaning_process('path_to_carx_directory', None)
