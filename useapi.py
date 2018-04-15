

import json
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_csvjson(filejson):
    # args[0] for json file path
    with open(filejson, 'r') as json_file:
        data = json.load(json_file)

    # store all keys
    users = [user for user in data.keys()]

    # store all values
    permissions1 = []
    for user in users:
        permissions1 += data[user]

    # remove duplicates
    permissions = set(permissions1)

    pms = [p for p in permissions]

    result = []
    for user in users:
        aa = [user]
        for pm in pms:
            if pm in data[user]:
                aa.append(1)
            else:
                aa.append(0)
        result.append(aa)
    # return 2d array and column names
    return result, pms

def writercsv(wpath,data,pms):
    # args[0] for write file path
    # args[1] for 2d array
    # args[2] for column name in csv
    with open(wpath, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['user'] + pms)
        writer.writerows(data)
        print('csv file is create')


def callGoogleApi(data,pms):
    # agrs[0] for 2d array, args[1] for column name list
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('helloworld').sheet1
    index=1
    sheet.insert_row(pms,index)
    
    for row in data:
        index +=1
        sheet.insert_row(row,index)
    print('google spreadsheet is updated')


if __name__ == '__main__':
    file_json="data.json"
    write_path="data2.csv"
    
    res,pms =get_csvjson(file_json)
    # write to csv file
    writercsv(write_path,res,pms)



    columns=['user']+pms
    # update to google spreadsheet
    # viriable res for 2d array, viriable columns for columns name
    callGoogleApi(res,columns)

    print('all done')

