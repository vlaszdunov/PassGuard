from ProgramData.Database import DataBase
from ProgramData.Password import Password
from ProgramData.AdditionalClass import Additional
from ProgramData.Application import Application
import os
Application()
DataBase()

while True:
    if Application.Return==False:
        if Application.SelectedMenuItem==-1:
            Application.MainMenu()
        match Application.SelectedMenuItem:
            case 0:
                Application.ShowData()
            case 1:
                Application.ExportData()
            case 2:
                os.system('cls||clear')
                NewPassword = Password._generate_password()
                print('Сгенерирован пароль: ', NewPassword)
                match Additional.Confirmation('Желайтее сохранить пароль?'):
                    case True:
                        NewSite = input('Введите URL сайта: ',)
                        NewLogin = input('Введите логин: ',)
                        DataBase.CreateDataObject(NewSite, NewLogin, NewPassword)
                    case False:
                        pass
            case 3:
                os.system('cls||clear')
                NewSite = input('Введите URL сайта: ',)
                NewLogin = input('Введите логин: ',)
                match Additional.Confirmation('Сгенерировать пароль автоматически?'):
                    case True:
                        DataBase.CreateDataObject(NewSite, NewLogin)
                    case False:
                        NewPassword = input('Введите собственный пароль: ',)
                        DataBase.CreateDataObject(NewSite, NewLogin, NewPassword)

            case 4:
                os.system('cls||clear')
                exit()
        Application.SelectedMenuItem=-1
    
    if Application.SelectedDataBaseItem < len(DataBase.Data) and Application.SelectedDataBaseItem != -1:
        Application.Return=False
        Application.ShowDataObject()
        match Additional.Select(Application.DataObjectMenuButtons):
            case 0:
                match Additional.Confirmation('Сгенерировать пароль автоматически?'):
                    case True:
                        DataBase.Data[Application.SelectedDataBaseItem].ChangePassword()
                    case False:
                        NewPassword = input('Введите собственный пароль: ',)
                        DataBase.Data[Application.SelectedDataBaseItem].ChangePassword(NewPassword)
                DataBase.SaveData()
                Application.Return=True
            case 1:
                NewSite = input('Введите адрес сайта: ',)
                DataBase.Data[Application.SelectedDataBaseItem].ChangeSite(NewSite)
                DataBase.SaveData()
                Application.Return=True
            case 2:
                NewLogin = input('Введите логин: ',)
                DataBase.Data[Application.SelectedDataBaseItem].ChangeLogin(NewLogin)
                DataBase.SaveData()
                Application.Return=True
            case 3:
                print(' ')
                match Additional.Confirmation('Вы точно хотите удалить эту запись?'):
                    case True:
                        DataBase.DeleteDataObject(
                            Application.SelectedDataBaseItem)
                    case False:
                        Application.Return=True
            case 4:
                Application.SelectedMenuItem=0
            case 5:
                os.system('cls||clear')
    elif Application.SelectedDataBaseItem >= len(DataBase.Data):
        os.system('cls||clear')
