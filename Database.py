import vars
import consts
import json
from Password import Password
if vars.AllowSpecSymbols == True:
    alphabet = consts.AlphabetWithSpecs
else:
    alphabet = consts.Alphabet


class DataBase:
    Data = {"Data": []}
    Passwords = []

    def __init__(self, FilePath) -> None:
        file = open(FilePath, 'r')
        self.Data = (json.loads(file.read()))
        file.close()

    def CreateDataObject(self):
        if len(self.Data['Data'])==0:
            self.Data['Data'].append(Password(0,
                          Password._generate_password(), 'q', 'a', 'c').__dict__)
        else:
            self.Data['Data'].append(Password(self.Data['Data'][-1]['Id']+1,
                          Password._generate_password(), 'q', 'a', 'c').__dict__)

    def ExportData(self, FilePath):
        file = open(FilePath, 'w')
        file.write(json.dumps(self.Data))
        file.close()

    def DeletePassword(self):
        pass

a=DataBase('Data.json')
a.CreateDataObject()
print(a.Data['Data'])