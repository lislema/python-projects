import os
import dropbox
import streamlit as st
from dotenv import load_dotenv
from dropbox.exceptions import AuthError

# Load environment variables from .env file
load_dotenv()

# Retrieve Dropbox access token from environment variable
ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')


# Function to upload the file to Dropbox
def upload_file_to_dropbox(local_file_path, file_name):
    """Uploads a file to Dropbox's root directory."""
    # Authenticate to Dropbox
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
    except AuthError as e:
        st.error(f"Error authenticating to Dropbox: {e}")
        return

    # Check if the file exists
    if not os.path.isfile(local_file_path):
        st.error(f"Error: The file {local_file_path} does not exist.")
        return

    # Upload file
    dropbox_path = f"/{file_name}"  # Default directory with original file name
    try:
        with open(local_file_path, "rb") as file:
            dbx.files_upload(file.read(), dropbox_path, mute=True)
        st.success(f"File '{file_name}' uploaded successfully to Dropbox at '{dropbox_path}'")
    except Exception as e:
        st.error(f"An error occurred while uploading the file: {e}")


# Streamlit UI
def main():
    st.title("Dropbox File Uploader")

    if not ACCESS_TOKEN:
        st.error("Dropbox API Access Token not found in environment variables. Please check your .env file.")
        return

    # File uploader
    uploaded_file = st.file_uploader("Choose a file to upload", type=None)

    if uploaded_file is not None:
        # Display file details
        st.write(f"File name: {uploaded_file.name}")
        st.write(f"File size: {uploaded_file.size / 1024:.2f} KB")

        if st.button("Upload"):
            # Save the file locally to use for uploading
            local_file_path = f"temp_{uploaded_file.name}"
            with open(local_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Upload to Dropbox (default root directory with original file name)
            upload_file_to_dropbox(local_file_path, uploaded_file.name)

            # Clean up the temp file after upload
            os.remove(local_file_path)


if __name__ == "__main__":
    main()