import os

def find_steam_library():
    steam_path = os.path.expandvars(r'%ProgramFiles(x86)%\Steam\steamapps\libraryfolders.vdf')
    if not os.path.exists(steam_path):
        raise FileNotFoundError("Steam library file not found.")
    
    with open(steam_path, 'r') as file:
        data = file.read()
    
    libraries = []
    for line in data.splitlines():
        if 'path' in line:
            path = line.split('"')[3]
            libraries.append(path)
    
    return libraries

def find_carx_directory():
    libraries = find_steam_library()
    for library in libraries:
        carx_path = os.path.join(library, 'steamapps', 'common', 'CarX Drift Racing Online')
        if os.path.exists(carx_path):
            return carx_path
    raise FileNotFoundError("CarX Drift Racing Online directory not found.")

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

if __name__ == "__main__":
    try:
        carx_directory = find_carx_directory()
        files = find_files_for_hashing(carx_directory, {'original_file1_hash', 'original_file2_hash'})
    except FileNotFoundError as e:
        print(e)
