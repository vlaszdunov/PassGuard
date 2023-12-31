from ProgramData.Database import DataBase
from ProgramData.Password import Password
from ProgramData.AdditionalClass import Additional
from ProgramData.Application import Application
import ProgramData.vars as vars
import os
Application()
DataBase()

while True:
    if Application.Return == False:
        Application.SelectedDataBaseItem = -1
        if Application.SelectedMenuItem == -1:
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
                        while Additional.InputChecker(NewSite, 'is_url') == False:
                            print('Неправильно введен URL')
                            NewSite = input(
                                'Введите URL в формате example.com: ',)

                        NewLogin = input('Введите логин: ',)
                        while Additional.InputChecker(NewLogin) == False:
                            print('Поле "Логин" не может быть пустым!')
                            NewLogin = input('Введите логин: ',)
                        DataBase.CreateDataObject(
                            NewSite, NewLogin, NewPassword)
                    case False:
                        pass
            case 3:
                os.system('cls||clear')
                NewSite = input('Введите URL сайта: ',)
                while Additional.InputChecker(NewSite, 'is_url') == False:
                    print('Неправильно введен URL')
                    NewSite = input('Введите URL в формате example.com: ',)

                NewLogin = input('Введите логин: ',)
                while Additional.InputChecker(NewLogin) == False:
                    print('Поле "Логин" не может быть пустым!')
                    NewLogin = input('Введите логин: ',)
                match Additional.Confirmation('Сгенерировать пароль автоматически?'):
                    case True:
                        DataBase.CreateDataObject(NewSite, NewLogin)
                    case False:
                        print(' ')
                        print('Пароль должен содержать',
                              vars.PassLength, 'символов')
                        NewPassword = input('Введите собственный пароль: ',)
                        while Additional.InputChecker(NewPassword, "length") == False:
                            print(' ')
                            print('Пароль не удовлетворяет требованиям')
                            print('Пароль должен содержать',
                                  vars.PassLength, 'символов')
                            NewPassword = input(
                                'Введите собственный пароль: ',)

                        DataBase.CreateDataObject(
                            NewSite, NewLogin, NewPassword)

            case 4:
                os.system('cls||clear')
                exit()
        Application.SelectedMenuItem = -1

    if Application.SelectedDataBaseItem < len(DataBase.Data) and Application.SelectedDataBaseItem != -1:
        Application.Return = False
        Application.ShowDataObject()
        match Additional.Select(Application.DataObjectMenuButtons):
            case 0:
                match Additional.Confirmation('Сгенерировать пароль автоматически?'):
                    case True:
                        DataBase.Data[Application.SelectedDataBaseItem].ChangePassword(
                        )
                    case False:
                        print('Пароль должен содержать',
                              vars.PassLength, 'символов')
                        NewPassword = input('Введите собственный пароль: ',)
                        while Additional.InputChecker(NewPassword, "length") != True:
                            print(' ')
                            print('Пароль не удовлетворяет требованиям')
                            print('Пароль должен содержать',
                                  vars.PassLength, 'символов')
                            NewPassword = input(
                                'Введите собственный пароль: ',)
                        DataBase.Data[Application.SelectedDataBaseItem].ChangePassword(
                            NewPassword)
                DataBase.SaveData()
                Application.Return = True
            case 1:
                NewSite = input('Введите адрес сайта: ',)
                while Additional.InputChecker(NewSite, 'is_url') == False:
                    print('Неправильно введен URL')
                    NewSite = input('Введите URL в формате example.com: ',)
                DataBase.Data[Application.SelectedDataBaseItem].ChangeSite(
                    NewSite)
                DataBase.SaveData()
                Application.Return = True
            case 2:
                NewLogin = input('Введите логин: ',)
                while Additional.InputChecker(NewLogin) == False:
                    print('Поле "Логин" не может быть пустым!')
                    NewLogin = input('Введите логин: ',)
                DataBase.Data[Application.SelectedDataBaseItem].ChangeLogin(
                    NewLogin)
                DataBase.SaveData()
                Application.Return = True
            case 3:
                print(' ')
                match Additional.Confirmation('Вы точно хотите удалить эту запись?'):
                    case True:
                        DataBase.DeleteDataObject(
                            Application.SelectedDataBaseItem)
                    case False:
                        Application.Return = True
            case 4:
                Application.SelectedMenuItem = 0
            case 5:
                os.system('cls||clear')
    elif Application.SelectedDataBaseItem >= len(DataBase.Data):
        os.system('cls||clear')
