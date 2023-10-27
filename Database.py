import vars
import consts
import json
from Password import Password
if vars.AllowSpecSymbols == True:
    alphabet = consts.AlphabetWithSpecs
else:
    alphabet = consts.Alphabet


class DataBase:
    Data = {}

    def __init__(self, FilePath) -> None:
        file = open(FilePath, 'r')
        self.Data.update(json.loads(file.read()))
        file.close()

    def CreateDataObject(self, object):
        self.Data['Data'].append(object.__dict__)

    def ExportData(self, FilePath):
        file = open(FilePath, 'w')
        file.write(json.dumps(self.Data))
        file.close()

    def DeletePassword(self):
        pass
