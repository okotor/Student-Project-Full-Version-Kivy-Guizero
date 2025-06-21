### Program imports
import datetime as dt
from datetime import date, datetime, timedelta
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError  # Assuming APIError is an alias for HttpError
import json
import os
from pathlib import Path
import pygame
import string

### Program configuration

## Working directory configuration
# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory
os.chdir(current_directory)
# Now you can perform operations in the current directory
print(f"Current working directory is: {os.getcwd()}")

## A Music file configuration
# Initialize pygame mixer
pygame.mixer.init()
# Load the music file
music_path = "app_advertisement.mp3"
pygame.mixer.music.load(music_path)

## Google Sheets database configuration
# Uncomment the line below to directly set the path for testing
SERVICE_ACCOUNT_FILE = r'service_account_key.json'
# Or use the environment variable (ensure it's set correctly in your environment)
# SERVICE_ACCOUNT_FILE = os.environ.get('service_account_key.json')
if SERVICE_ACCOUNT_FILE is None:
    raise ValueError("The service account file path is not set. Please set the SERVICE_ACCOUNT_FILE environment variable or provide the path directly.")
# Define the scopes for Google Drive and Google Sheets
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
# Authenticate using the service account
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# Google Drive API client
drive_service = build('drive', 'v3', credentials=creds)
# Google Sheets API client
gc = gspread.authorize(creds)
# Folder ID of the Google Drive folder where you want to create the sheet
folder_id = '1sItL5XHj10mVqDj0RA90O8jd7qoC1Zy0'  # Replace with your actual folder ID
# sheet_name = 'A Brand New Spreadsheet'