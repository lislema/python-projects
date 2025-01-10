import os
import tarfile
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    # Generate a unique filename based on the current timestamp
    backup_filename = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.tar.gz"
    backup_filepath = os.path.join(backup_dir, backup_filename)

    # Create the tar.gz file and add the source directory
    with tarfile.open(backup_filepath, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    print(f"Backup completed: {backup_filepath}")

if __name__ == "__main__":
    # Prompt the user for source and destination directories
    source = input("Enter the source directory to back up: ").strip()
    destination = input("Enter the destination directory to store the backup: ").strip()

    # Validate that the source directory exists
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist.")
    # Validate that the destination directory exists
    elif not os.path.exists(destination):
        print(f"Error: Destination directory '{destination}' does not exist.")
    else:
        # Run the backup process
        backup_directory(source, destination)