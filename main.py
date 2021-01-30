import os

from dotenv import load_dotenv
load_dotenv()

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from upload import upload

print("Authorizing...")
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

FILES_DIR = os.getenv("FILES_DIR", "")
REMOTE_DIR_ID = os.getenv("REMOTE_DIR_ID")
UPLOAD_LIST_PATH = "upload_list.json"

upload(drive, UPLOAD_LIST_PATH, REMOTE_DIR_ID, FILES_DIR)
print("Successfully uploaded!")
