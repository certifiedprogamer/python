import os

directory_path = '.\\rps_resources\\'
output_file_path = '.\\rps_resources\\rps.log'

files = os.listdir(directory_path)

# Filter files if needed (e.g., open only text files)
files = [f for f in files if f.endswith('.rps')]


with open(output_file_path, 'w') as output_file:
    # Process each file in the directory
    for file_name in files:
        # get the file path of the file that's going to be written to rps.log
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'r') as file:
            content = file.read()  # Read content of the file
            # Write the content to the output file, each on a new line
            # Add newline after each file's content
            output_file.write(content + '\n')

print(f"Contents of the files have been written to {output_file_path}")
