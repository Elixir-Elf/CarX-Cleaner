import os
import shutil
from datetime import datetime
import time

def create_backup_directory(base_directory):
    backups_directory = os.path.join(base_directory, 'Backups')
    if not os.path.exists(backups_directory):
        os.makedirs(backups_directory)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_directory = os.path.join(backups_directory, timestamp)
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    return backup_directory

def backup_file(file_path, backup_directory, retries=5, delay=10):
    for attempt in range(retries):
        try:
            relative_path = os.path.relpath(file_path, backup_directory)
            backup_path = os.path.join(backup_directory, relative_path)
            backup_dir = os.path.dirname(backup_path)
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            shutil.copy2(file_path, backup_path)
            return
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                print(f"Error backing up file {file_path}: {e}")

def backup_files(files, backup_base_directory):
    backup_directory = create_backup_directory(backup_base_directory)
    for file in files:
        backup_file(file, backup_directory)
    return backup_directory
