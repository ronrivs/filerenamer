import os
import re

# Set the path where the files are
path = r"YOUR LOCAL DRIVE"

# Go through each file in the directory
for filename in os.listdir(path):
    # Check if the file name contains 'word'
    if 'WORD' in filename:
        # Replace 'word' with 'word2'
        new_filename = re.sub('WORD', 'WORD2', filename)
        
        # Get the full file paths
        old_file_path = os.path.join(path, filename)
        new_file_path = os.path.join(path, new_filename)

        # Rename the files
        os.rename(old_file_path, new_file_path)
