import os
import datetime

def categorize_files_by_age(directory):
    """ Categorize files in a given directory and its subdirectories based on their age """
    now = datetime.datetime.now()
    file_age_data = {
        "less_than_week": [],
        "week_to_month": [],
        "older_than_month": []
    }

    oldest_file = None
    newest_file = None
    oldest_time = None
    newest_time = None

    for root, _ , files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                # Get creation time
                creation_time = os.path.getctime(file_path)
                creation_date = datetime.datetime.fromtimestamp(creation_time)

                # Determine file age category
                age_days = (now - creation_date).days
                if age_days < 7:
                    file_age_data["less_than_week"].append(file_path)
                elif 7 <= age_days < 30:
                    file_age_data["week_to_month"].append(file_path)
                else:
                    file_age_data["older_than_month"].append(file_path)

                if oldest_time is None or creation_date < oldest_time:
                    oldest_file = file_path
                    oldest_time = creation_date

                if newest_time is None or creation_date > newest_time:
                    newest_file = file_path
                    newest_time = creation_date


            except OSError as e:
                print(f"Could not process file {file_path}: {e}")

    return file_age_data, oldest_file, newest_file, oldest_time, newest_time

def display_report(file_age_data, oldest_file, newest_file, oldest_time, newest_time):
    """ Display the summary report of file age analysis  """

    print("\n---File Age Analysis Report---")
    print(f"Files created less than a week ago: {len(file_age_data['less_than_week'])}")
    print(f"Files created between a week and a month ago: {len(file_age_data['week_to_month'])}")
    print(f"Files older than a month: {len(file_age_data['older_than_month'])}")
    
    if oldest_file and oldest_time :
        print(f"Oldest file: {oldest_file} (Created: {oldest_time})")
    if newest_file and newest_time :
        print(f"Newest file: {newest_file} (Created: {newest_time})")
    print("\nAnalysis complete!")
    
if __name__ == "__main__":
    print("Welcome to File Age Analyser")
    directory = input("Enter a directory path to analyse: ")
    
    if not(os.path.isdir(directory)):
        print("Invalid directory - the provided path is not a  directory or does not exist")
    else:
        print("Analyzing directory, please wait... ")
        file_age_data, oldest_file, newest_file, oldest_time, newest_time = categorize_files_by_age(directory)
        display_report(file_age_data, oldest_file, newest_file, oldest_time,newest_time)