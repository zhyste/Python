import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time
#needs the json file in the same folder
x = 2
Name = 'Shan' #finds the person name in the spreadsheet
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive'] #googlesheet api

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json.json', scope) #needs ur json file
client = gspread.authorize(creds)

pp = pprint.PrettyPrinter()
sheet = client.open_by_url('the url of your google sheet').sheet1 
pp = pprint.PrettyPrinter()
cells = sheet.find(Name)
value = cells.value
row_number = cells.row
column_number = cells.col
values_list = sheet.row_values(cells.row)

pp.pprint("Found something at R%sC%s" % (cells.row, cells.col))

print (column_number)

money = sheet.cell(row_number, 27) .value 

Postal = sheet.cell(row_number, 5).value

location = sheet.cell(row_number, 4).value

fee = sheet.cell(row_number , 26).value


print ('Hi',Name,', thank you for your order. I’m Joe here, helping Ryan to coordinate the orders \n \nKindly make payment of $*'+ money + '* (which includes $'+ fee + ' delivery fee) via paylah or paynow to Ryan at 999999999. Pls send me a *Screenshot* of the receipt so that we can arrange for your delivery.')


print('\nOrder Details:')

Soymilk = sheet.cell(row_number , 7).value
if Soymilk is (""):
    x = 2 
else:
    int_Soymilk = int(Soymilk)
    print(int_Soymilk,'X Soya Milk ($1.50 each)')  

SoyMilkLess = sheet.cell(row_number , 8).value
if SoyMilkLess is (""):
    x = 2 
else:
    int_SoyMilkLess = int(SoyMilkLess)
    print(int_SoyMilkLess, 'X Soy Milk Less Sugar ($1.50 each)')


SoyMilkNo = sheet.cell(row_number , 9).value
if SoyMilkNo is (""):
    x = 2 
else:
    int_SoyMilkNo = int(SoyMilkNo)
    print(int_SoyMilkNo, 'X Soy Milk No Sugar ($1.50 each)')



HoneyGinger = sheet.cell(row_number , 10).value
if HoneyGinger is (""):
    x = 2 
else:
    int_HoneyGinger = int(HoneyGinger)
    print(int_HoneyGinger, 'X Honey Ginger ($2 each)')

GingerExtract = sheet.cell(row_number , 11).value
if GingerExtract is (""):
    x = 2 
else:
    int_GingerExtract =int(GingerExtract)
    print(int_GingerExtract, 'X Ginger Extract ($5 each)')




Kombucha = sheet.cell(row_number , 12).value
if Kombucha is (""):
    x = 2 
else:
    int_Kombucha = int(Kombucha)
    print(int_Kombucha, 'X Kombucha ($15 per bottle)')

Beancurd = sheet.cell(row_number , 13 ).value

if Beancurd is (""):
    x = 2 
else:
    int_Beancurd = int(Beancurd)
    print(int_Beancurd, 'X Beancurd ($1.50 each)')





JellyBeancurd = sheet.cell(row_number , 14 ).value

if JellyBeancurd is (""):
    x = 2 
else:
    int_JellyBeancurd = int(JellyBeancurd)
    print(int_JellyBeancurd, 'X Jelly Beancurd ($1.50 each)')




JellBeancurdAlmond = sheet.cell(row_number , 15).value

if JellBeancurdAlmond is (""):
    x = 2 
else:
    int_JellBeancurdAlmond = int(JellBeancurdAlmond)
    print(int_JellBeancurdAlmond, 'X Jelly Beancurd Almond ($1.50 each)')



JellyBeancurdBandung = sheet.cell(row_number , 16).value 

if JellyBeancurdBandung is (""):
    x = 2 
else:
    int_JellyBeancurdBandung = int(JellyBeancurdBandung)
    print(int_JellyBeancurdBandung, 'X Jelly Beancurd Bandung ($1.50 each)')





JellybeancurdChoc = sheet.cell(row_number , 17).value

if JellybeancurdChoc is (""):
    x = 2
else:
    int_JellybeancurdChoc = int(JellybeancurdChoc)
    print(int_JellybeancurdChoc, 'X Jelly Beancurd Chocolate ($1.50 each)')




GrassJelly = sheet.cell(row_number, 18 ).value

if GrassJelly is (""):
    x = 2
else: 
    int_GrassJelly = int(GrassJelly)
    print(int_GrassJelly, 'X Grass Jelly ($1.50 each)')






IceJelly = sheet.cell(row_number, 19).value

if IceJelly is (""):
    x = 2
else: 
    int_IceJelly = int(IceJelly)
    print(int_IceJelly,'X Ice Jelly ($1.50 each)')



Charsiew = sheet.cell(row_number , 20).value

if Charsiew is (""):
    x = 2
else: 
    int_Charsiew = int(Charsiew)
    print(int_Charsiew, 'X Charsiew ($0.70 each)')






LorMaiGai = sheet.cell(row_number , 21).value

if LorMaiGai is (""):
    x = 1
else:
    int_LorMaiGai = int(LorMaiGai)
    print(int_LorMaiGai, 'X Lor Mai Gai ($1.50 each)')



FanChoi = sheet.cell(row_number , 22).value

if FanChoi is (""):
    x = 2
else:
    int_FanChoi = int(FanChoi)
    print(int_FanChoi,  'X Fan Choi($1.80 each)')


BeancurdLess = sheet.cell(row_number , 23).value

if BeancurdLess is (""):
    x = 2
else:
    int_BeancurdLess = int(BeancurdLess)
    print(int_BeancurdLess, 'X Beancurd Less Sugar ($1.50 each)')


BeancurdNo = sheet.cell(row_number , 24).value

if BeancurdNo is (""):
    x = 2
else:
    int_BeancurdNo = int(BeancurdNo)
    print(int_BeancurdNo, 'X Beancurd No Sugar ($1.50 each)')





print('\nTotal: $'+ money + ' (which includes $'+ fee + ' delivery fee)')
print('\nDelivery Address is: ' + location, '' + Postal)

print('\nThank you!\n \nJoe \nFood Company Singapore')
