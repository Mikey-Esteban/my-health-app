from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
import io
import os

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Obtain your Google credentials
def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file('../secrets/desktop_google_client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

# Build the downloader
creds = get_credentials()
drive_downloader = build('drive', 'v3', credentials=creds)

# Replace 'FOLDER_ID' with your actual Google Drive folder ID
folder_id = '1ba7lJZw2i_am8Vgm993eekipQb-WHlAu'

# query = f"Folder ID '{folder_id}'"  # you may get error for this line
query = f"'{folder_id}' in parents"  # this works  ref https://stackoverflow.com/q/73119251/248616

results = drive_downloader.files().list(q=query, pageSize=1000).execute()
items = results.get('files', [])

# Download the files
for item in items:
    request = drive_downloader.files().get_media(fileId=item['id'])
    f = io.FileIO(item['name'], 'wb')
    downloader = MediaIoBaseDownload(f, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}.")

print(f"Downloaded {len(items)} files from the folder.")