import csv
dates = ["28-Jul-2016", "25-Aug-2016", "29-Sep-2016"]
companies = ["NTPC", "UNIONBANK", "PETRONET", "IGL", "PFC", "RECLTD", "MINDTREE", "INDUSINDBK", "DALMIABHA", "LUPIN", "TITAN", "GRASIM"]
finalfile = open('results.csv', 'w')
fieldnames = ['TRADE_DT', 'SYMBOL', 'EXPIRY_DT','OPTION_TYP', 'HIGH']
writer = csv.DictWriter(finalfile, fieldnames=fieldnames)
writer.writeheader()
filedate = '040716'
csvfile = open('gg.csv', 'r')
read = csv.DictReader(csvfile)
reader = list(read)
for company in companies:
    for date in dates:
        for opt in ['CE', 'PE']:
        	high = []
        	for row in reader:
        		if(row['INSTRUMENT'] == "OPTSTK"):
        			if (row['SYMBOL'] == company):
        				if (row['EXPIRY_DT'] == date):
        					if (row['OPTION_TYP'] == opt):
        						high.append(row['HIGH'])
        	high = map(float, high)
        	high.sort(reverse=True)
        	if(len(high)>9):
	        	for i in range(0,10):
	        		writer.writerow({'TRADE_DT': filedate, 'SYMBOL': company, 'EXPIRY_DT' : date, 'OPTION_TYP' : opt, 'HIGH' : high[i] })     


