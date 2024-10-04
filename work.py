import pathlib
import hashlib
import os

def compute_file_hash(file_path):
    # Create an instance of hashlib with the algorithm = sha256
    hash_func = hashlib.new(algorithm='sha256')    
    
    with open(file_path, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        #chunk = file.read(8192)
        while chunk := file.read(8192):    
            #chunk = file.read(8192)
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def check_destination(source_file_path, current_source_file, subdirectory):
    base_dest_path = r"D:\IT260" 
    # if the subdirectory equals to the root directory we remove it
    if subdirectory == ".":
        subdirectory = ""

    dest_file_path = os.path.join(base_dest_path, subdirectory,current_source_file)

    
    if os.path.exists(source_file_path) and os.path.exists(dest_file_path):
        if compute_file_hash(source_file_path) == compute_file_hash(dest_file_path):
            print(f"File {current_source_file} matches")
        else:
            print(f"File {current_source_file} does not match")
    else:
        print(f"File {current_source_file} does not exist in one of the locations")


source_dir = r"D:\SNHU\IT260"  # Source Directory
dest_dir = r"D:\IT260"  # Destination directory

for root, dirs, files in os.walk(source_dir):
    # Current subdirectory, later will be passed to the check destination function, to be concatenated to base destination folder
    current_subdirectory = os.path.relpath(root, source_dir)
    for file in files:
        # Current source file path
        source_file_path = os.path.join(root, file)  
        # Call the check destination file function
        check_destination(source_file_path, file, current_subdirectory)    
        
       
