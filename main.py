from Password import Password
from Database import DataBase
from Application import Application
import cutie
b = DataBase('Data.json')
a = Application(b)
# print('пароль= ', b.Data['Data'][a.MainMenu()]['Value'])
# print(b.MaxLoginLen)
while True:
    a.MainMenu(b)
    a.ShowDatabaseItem(b)
