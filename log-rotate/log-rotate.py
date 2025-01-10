import os
import shutil
from datetime import datetime

def rotate_log_file(logfile, backup_dir):
    if os.path.exists(logfile):
        # Generate a timestamped backup filename
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_log = os.path.join(backup_dir, f"log_{timestamp}.log")

        # Move the log file to the backup directory and create a new empty log file
        shutil.move(logfile, backup_log)
        open(logfile, 'w').close()  # Create a new empty log file

        print(f"Log rotated and saved as {backup_log}")
    else:
        print(f"{logfile} does not exist.")

if __name__ == "__main__":
    # Prompt the user for the log file and backup directory
    logfile = input("Enter the path to the log file: ").strip()
    backup_dir = input("Enter the backup directory: ").strip()

    # Validate that the backup directory exists
    if not os.path.exists(backup_dir):
        print(f"Error: Backup directory '{backup_dir}' does not exist.")
    else:
        # Perform log rotation
        rotate_log_file(logfile, backup_dir)