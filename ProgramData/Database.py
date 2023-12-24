import json
import os
from ProgramData.Password import Password


class DataBase:
    Data = []

    @staticmethod
    def __init__() -> None:
        if os.path.exists(r'ProgramData/Data.json') == False:
            file = open(r'ProgramData/Data.json', 'w')
            file.write(json.dumps({"Data": []}))
            file.close()

        file = open(r'ProgramData/Data.json', 'r')
        for DataRow in json.loads(file.read())['Data']:
            DataBase.Data.append(Password(
                DataRow['Id'], DataRow['Site'], DataRow['Login'], DataRow['Password']))
        file.close()

    def CreateDataObject(newsite, newlogin, password=None):
        if password == None:
            if len(DataBase.Data) == 0:
                DataBase.Data.append(Password(0, newsite, newlogin))
            else:
                DataBase.Data.append(
                    Password(DataBase.Data[-1].Id+1, newsite, newlogin))
        else:
            if len(DataBase.Data) == 0:
                DataBase.Data.append(Password(0, newsite, newlogin, password))
            else:
                DataBase.Data.append(
                    Password(DataBase.Data[-1].Id+1, newsite, newlogin, password))
        DataBase.SaveData()

    def DataPreparation():
        PreparedData = {"Data": []}
        for DataRow in DataBase.Data:
            PreparedData['Data'].append(DataRow.__dict__)
        return PreparedData

    def ExportData():
        file = open(r'C:\Users\\'+os.getlogin() +
                    r'\Downloads\ExportedData.json', 'w')

        file.write(json.dumps(DataBase.DataPreparation()))
        file.close()

    def DeleteDataObject(DataIndex):
        DataBase.Data.pop(DataIndex)
        DataBase.SaveData()
        os.system('cls||clear')

    def SaveData():
        file = open(r'ProgramData/Data.json', 'w')
        file.write(json.dumps(DataBase.DataPreparation()))
        file.close()
