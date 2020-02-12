#одключение к GOOGLE Drive
import gspread
from oauth2client.service_account import ServiceAccountCredentials

key ="c:\KEY\investingmoex-cb91da954760.json"

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(key, scope)
client = gspread.authorize(creds)
sheet = client.open("t1").sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)