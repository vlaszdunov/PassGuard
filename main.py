from Password import Password
from Database import DataBase
import cutie
data = DataBase('Data.json')
datalist = []
# for i in data.Data['Data']:
#     datalist.append(i['Site']+'     '+i['Login'])


# def main():
#     print('')
#     print('ВАШИ ПАРОЛИ')
#     print('------------------')
#     d = cutie.select(datalist)
#     print(d)


# main()
a = DataBase('Data.json')
a.CreateDataObject()
print(a.Data['Data'])
a.CreateDataObject()
print(a.Data['Data'])
