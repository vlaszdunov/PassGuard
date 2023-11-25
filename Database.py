import vars
import consts
import json
import os
from random import randint
from Password import Password
if vars.AllowSpecSymbols == True:
    alphabet = consts.AlphabetWithSpecs
else:
    alphabet = consts.Alphabet


class DataBase:
    Data = {"Data": []}
    MaxSiteLen = 4
    File = 'Data.json'

    @staticmethod
    def __init__() -> None:
        file = open(DataBase.File, 'r')
        DataBase.Data = (json.loads(file.read()))
        file.close()
        for i in DataBase.Data['Data']:
            if len(i['Site']) > DataBase.MaxSiteLen:
                DataBase.MaxSiteLen = len(i['Site'])

    def CreateDataObject(newlogin, newsite):
        if len(DataBase.Data['Data']) != 0:
            DataBase.Data['Data'].append(Password(
                DataBase.Data['Data'][-1]['Id']+1, Password._generate_password(), newlogin, newsite).__dict__)
        else:
            DataBase.Data['Data'].append(Password(
                0, Password._generate_password(), newlogin, newsite).__dict__)

        DataBase.SaveData()

    def ExportData():
        file = open(r'C:\Users\socia\Downloads\ExportedData.txt', 'w')
        file.write(json.dumps(DataBase.Data))
        file.close()

    def DeleteDataObject(data_index):
        DataBase.Data['Data'].pop(data_index)
        DataBase.SaveData()

    def SaveData():
        file = open(DataBase.File, 'w')
        file.write(json.dumps(DataBase.Data))
        file.close()
