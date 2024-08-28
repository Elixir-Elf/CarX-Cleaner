import os
import json
import shutil
import time
from src.helpers.find import find_files_for_hashing
from src.helpers.backup import backup_files

def load_original_hashes(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)

def clean_files(directory, original_files, modded_files, backup_directory, progress_bar):
    total_files = len(modded_files)
    for index, file in enumerate(modded_files):
        relative_file = os.path.relpath(file, directory)
        if relative_file not in original_files:
            try:
                backup_file_path = os.path.join(backup_directory, relative_file)
                backup_dir = os.path.dirname(backup_file_path)
                if not os.path.exists(backup_dir):
                    os.makedirs(backup_dir)
                shutil.copy2(file, backup_file_path)
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
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f"Error deleting directory {dir_path}: {e}")

def start_cleaning_process(game_directory, backup_base_directory, progress_bar=None):
    original_hashes = load_original_hashes('src/hashes/relative_hashes.txt')
    original_files = set(original_hashes.keys())
    modded_files = find_files_for_hashing(game_directory, original_files)
    
    if not modded_files:
        print("No modded files found. The directory is either empty or all files are original.")
        return
    
    backup_directory = backup_files(modded_files, backup_base_directory)
    
    time.sleep(10)
    
    clean_files(game_directory, original_files, modded_files, backup_directory, progress_bar)
