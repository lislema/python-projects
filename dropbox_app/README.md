# Dropbox App 

a web app that any user can use to upload files to a Dropbox account

The web app lets the user upload a file. Once the user uploads a file and presses the “Upload” button, the app will be stored inside the “Apps” folder in your Dropbox account. 

## Pre-requisites 

Required Libraries: dropbox, streamlit, python-dotenv
```
pip install dropbox python-dotenv streamlit
```
This solution includes the steps to get a Dropbox token from your Dropbox account, storing the token securely using dotenv, and building the web app with Streamlit:

## Getting the Dropbox token and setting up 

- Login to your Dropbox account at https://www.dropbox.com
- Go to Dropbox App Console: https://www.dropbox.com/developers/apps
- Press “Create App” button.
- Set the settings, scoped access & folder. then name the Apps  and press “Create App”. 
- Go to the “Permissions” tab and check the **file.content.write** and **file.content.read** options to allow the app to view and add new files to your Dropbox folder. Then, press “Submit”.
- Go to the “Settings” tab and press the “Generate” button in the “Generate access token” section. Then, copy the generated token. 
- Copy the token and paste in a ".env" file 

```
DROPBOX_ACCESS_TOKEN=<Your-Token>
```
- Save the .env file 

## Run the Streamlit app 

Type in you terminal 

```
streamlit run main.py
```
Then visit http://localhost:8501 on your browser to view and use the web app.