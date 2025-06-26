# Fat Burner App - Google Sheets, Simple Version (Mobile/Tablet/Desktop)

This is a mobile/tablet/desktop app to track your weight, fat level and calorie intake/burn using the kivy or guizero GUI.


## Features

- Registering and Logging In Multiple Users
- For Each User:
 1. Calculating Fat Level based on Weight and Skinfolds for each
 2. Saving all Your Data in Your Online Google Sheet with just one click


## Prerequisites

- Python 3.x
- kivy
- guizero
- gspread
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- guizero
- pygame
- requests
- setuptools


## Installation

- Test the app's functionalities using the existing service_account_key.json by opening the folder in VS code and launching the 
    "simple_gui_desktop.py" for the guizero GUI or the "simple_gui_mobile.py" for the kivy GUI. Open the corresponding google folder to check the records (
        https://drive.google.com/drive/folders/1RxX80Imkk1n_pyu1GneC4VfYuS1A8nxo
    ) or the sheet itself (
        https://docs.google.com/spreadsheets/d/1wvQfVCq6EjuzSytYNeJivSr0Pq8FANYZsTYffbWnAbU/edit?gid=0#gid=0
    )
- Set up your Google Service Account Key on Google Cloud and download the service_account_key.json
- Create a folder and a Google Sheet granting access rights to the service account.
- Enter the correct Google data in the ./app/"config.py" file of this app.
- Open the project in VS code and run the ./app/"gui_mobile.py" file of. this app.

