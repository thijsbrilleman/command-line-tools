import os
import argparse

def read_and_print_file(file_path, base_directory):
    """Read the contents of a file and print it in the specified format."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
        relative_path = os.path.relpath(file_path, base_directory)
        print(f"{relative_path}:\n")
        print("```\n" + contents + "\n```\n")
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")

def process_directory(directory):
    """Recursively process a directory, printing the contents of each file."""
    for root, dirs, files in os.walk(directory):
        # Filter out hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
            file_path = os.path.join(root, file)
            read_and_print_file(file_path, directory)

def main():
    parser = argparse.ArgumentParser(description="Recursively output the contents of all files in a directory.")
    parser.add_argument('directory', type=str, help='The directory to process')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"The provided path '{args.directory}' is not a directory.")
        return

    process_directory(args.directory)

if __name__ == "__main__":
    main()
