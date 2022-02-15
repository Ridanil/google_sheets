import os.path
import re

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, "credentials.json")

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1tevcPXVxUGB9FRbEvltZI6ogmK_7CnELWcClrpKlIZk'
SAMPLE_RANGE_NAME = 'Лист1'

service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()


# result = sheet.get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                     range=SAMPLE_RANGE_NAME,
#                     majorDimension='COLUMNS').execute()

# data_from_sheet = result.get('values', [])
#print(data_from_sheet)

# range_ = "Лист1!A3:B4"
# array = {"values": [[5, 5], [5, 5]]}
# response = service.update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#                             range=range_,
#                             valueInputOption="USER_ENTERED", 
#                             body=array).execute()

def function(range_ = "Лист1!A2:d7", array = {"values": [[1, None, None, 2], []]}):
    # range_ = "Лист1!A8"
    # array = {"values": [[1, 2], [3, 4]]}
    response = service.update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                            range=range_,
                            valueInputOption="USER_ENTERED", 
                            body=array).execute()
    

function("Лист1!A2:d7", {"values": [[100,None, None, 1200], [ None, ]]})