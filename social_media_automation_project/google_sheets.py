
#module to connect to google sheets with google sheets api 
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheets:
    """Class for accessing google sheets
    methods:
        get_sheet_data: gets the data from the google sheet in raw JSON string format"""
    def __init__(self,project_name:str,sheet_name:str,json_file:str)->None:
        """Generates connection to google sheets with the given json cred file and sheet name
        Args:
            project_name (str): name of the google sheet project
            sheet_name (str): name of the google sheet
            json_file (str): path to the json file containing the google sheet creds
        Returns:
            None
        
        Attributes Generated :
            client (gspread.client): client object for accessing google sheets

        """
        self.project_name = project_name
        self.sheet_name = sheet_name
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, self.scope)
        self.client = gspread.authorize(self.creds)

    def get_sheet_data(self):
        """Gets the data from the google sheet in raw JSON string format"""
        sheet = self.client.open(self.project_name).worksheet("Sheet1")
        data = sheet.get_all_records()
        return data


