from read_spreadsheets import spreadsheet_helper
from apiclient import discovery
import httplib2

class Service:
    def __init__(self):
        self.sh = spreadsheet_helper()
        self.c = self.sh.get_credentials()
        self.http = self.c.authorize(httplib2.Http())
        self.service = discovery.build('drive','v3',http=self.http)
        self.folderMimes=['application/vnd.google-apps.folder']
        self.lstMimes = ['application/vnd.google-apps.spreadsheet','text/csv','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
    def getFolders(self):
        self.results = self.service.files().list(pageSize=1000).execute()
        self.filteredFolders = [x for x in self.results['files'] if x['mimeType'] in self.folderMimes]
        return [x['name'] for x in self.filteredFolders]
    def beginCleanup(self,folderNumber):
        return True
    def getResults(self):
        return["something","something else"]
    def login(self):
        return True