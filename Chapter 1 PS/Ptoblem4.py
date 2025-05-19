import os

# Specify the directory path; '.' refers to the current directory
directory_path = '/'

# Get the list of all files and directories
entries = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for entry in entries:
    print(entry)
