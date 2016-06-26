from read_spreadsheets import spreadsheet_helper
from apiclient import discovery
import httplib2

sh = spreadsheet_helper()
c = sh.get_credentials()
http = c.authorize(httplib2.Http())
service = discovery.build('drive','v3',http=http)
results = service.files().list(pageSize=1000).execute()
#print results
folderMimes=['application/vnd.google-apps.folder']
lstMimes = ['application/vnd.google-apps.spreadsheet','text/csv','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
filteredSpreadSheets = [x for x in results['files'] if x['mimeType'] in lstMimes]
filteredFolders = [x for x in results['files'] if x['mimeType'] in folderMimes]