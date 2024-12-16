import os

def analyze_folder(my_directory):

    """
    Analyze a folder and its subdirectories to rank files by size.
    """
    my_file_info = []

    # Traverse the directory and collect file information
    for root, _, files in os.walk(my_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)  # Get file size in bytes
                my_file_info.append((file_path, size))
            except OSError as e:
                print(f"Could not access file: {file_path} - {e}")

    # Sort files by size in descending order
    my_file_info.sort(key=lambda x: x[1], reverse=True)

    return my_file_info


def display_results(file_information, top_n=10):
    """
    Display results of the folder analysis.
    """
    total_size = sum(size for _, size in file_information)
    total_files = len(file_information)

    print("\n--- Folder Analysis Report ---")
    print(f"Total Files: {total_files}")
    print(f"Total Storage Used: {total_size / (1024 ** 2):.2f} MB\n")

    print(f"Top {top_n} Largest Files:")
    for i, (file_path, size) in enumerate(file_info[:top_n], 1):
        print(f"{i}. {file_path} - {size / (1024 ** 2):.2f} MB")


# Input directory from the user
print("Welcome to Local Folder Analyzer!")
directory = input("Enter the path of the folder to analyze: ")

if not os.path.isdir(directory):
    print("Error: The provided path is not a directory or does not exist.")
else:
    file_info = analyze_folder(directory)
    display_results(file_info)