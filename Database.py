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
    MaxLoginLen=0
    MaxSiteLen=0

    def __init__(self, FilePath) -> None:
        file = open(FilePath, 'r')
        self.Data = (json.loads(file.read()))
        file.close()
        for i in self.Data['Data']:
            if len(i['Login'])>self.MaxLoginLen:
                self.MaxLoginLen=len(i['Login'])
            if len(i['Site'])>self.MaxSiteLen:
                self.MaxSiteLen=len(i['Site'])

    def CreateDataObject(self):
        if len(self.Data['Data']) == 0:
            self.Data['Data'].append(Password(0,
                                              Password._generate_password(), 'q', 'a', 'c').__dict__)
        else:
            self.Data['Data'].append(Password(self.Data['Data'][-1]['Id']+1,
                                              Password._generate_password(), 'q', 'a', 'c').__dict__)

    def ExportData(self, FilePath):
        file = open(FilePath, 'w')
        file.write(json.dumps(self.Data))
        file.close()

    def DeletePassword():
        pass
