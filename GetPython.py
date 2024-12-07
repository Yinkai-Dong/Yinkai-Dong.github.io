import os

# Define the directory to scan (current directory by default)
directory = '.'

# Define the output file
output_file = 'files.txt'

# List of files to ignore (you can specify full paths or just file names)
ignore_files = ['main_full.py', 'GetPython.py', 'GetMatlab.py', 'GetFileAff.py'] 

# Open the output file to write
with open(output_file, 'w', encoding='utf-8', errors='ignore') as f:
    # Walk through the specified directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') :
                # Get the full path of the file
                full_path = os.path.join(root, file)
                
                # Check if the file or its full path is in the ignore list
                if file in ignore_files or os.path.relpath(full_path, directory) in ignore_files:
                    print(f"Skipping {full_path} (ignored)")
                    continue  # Skip this file
                
                print(f"Processing {full_path}...")

                # Write file path and name to the output file
                f.write(f"File Path: {full_path}\n")
                f.write(f"File Name: {file}\n")
                
                # Write file content to the output file with encoding handling
                f.write("File Content:\n")
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as file_content:
                    f.write(file_content.read())
                
                # Add a separator between files for clarity
                f.write("\n" + "="*50 + "\n\n")

print(f"All specified .py files' paths, names, and contents have been saved in {output_file}")
