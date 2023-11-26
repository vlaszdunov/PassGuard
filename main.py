from Password import Password
from Database import DataBase
from Application import Application
import cutie
import os
Application()
DataBase()


while True:
    Application.MainMenu()
    match Application.SelectedMenuItem:
        case 0:
            os.system('cls||clear')
            Application.ShowData()
        case 1:
            DataBase.ExportData()
        case 2:
            os.system('cls||clear')
            print('')
            print('Сгенерированный пароль: ', Password._generate_password())
            match cutie.prompt_yes_or_no('Сохранить пароль?', yes_text='Да', no_text='Нет', enter_empty_confirms=False, char_prompt=False):
                case True:
                    NewSite = input('Адрес сайта: ',)
                    NewLogin = input('Логин/почта: ',)
                    DataBase.CreateDataObject(NewLogin, NewSite)
                    DataBase.SaveData()
                case False:
                    pass
            os.system('cls||clear')

        case 3:
            os.system('cls||clear')
            NewSite = input('Адрес сайта: ',)
            NewLogin = input('Логин/почта: ',)
            DataBase.CreateDataObject(NewLogin, NewSite)
            DataBase.SaveData()
        case 4:
            os.system('cls||clear')
            exit()

    if Application.SelectedDataBaseItem != -1:
        os.system('cls||clear')
        Application.ShowDataObject()
        print('')
        print('Выберите действие')
        print('─'*20)
        Application.SelectedMenuItem = cutie.select(
            Application.DataMenuButtons)

        match Application.SelectedMenuItem:
            case 0:
                os.system('cls||clear')
                DataBase.Data['Data'][Application.SelectedDataBaseItem]['Password'] = Password._generate_password(
                )
                print('')
                print('Для учетной записи с логином', DataBase.Data['Data'][Application.SelectedDataBaseItem]
                      ['Login'], 'на сайте', DataBase.Data['Data'][Application.SelectedDataBaseItem]['Site'])
                print('Был создан новый пароль: ',
                      DataBase.Data['Data'][Application.SelectedDataBaseItem]['Password'])

            case 1:
                print('')
                DataBase.Data['Data'][Application.SelectedDataBaseItem]['Site'] = input(
                    'Введите новый адрес сайта: ',)

            case 2:
                print('')
                DataBase.Data['Data'][Application.SelectedDataBaseItem]['Login'] = input(
                    'Введите новый логин: ',)

            case 3:
                match cutie.prompt_yes_or_no('Удалить запись?', yes_text='Да, удалить', no_text='Нет, оставить', enter_empty_confirms=False, char_prompt=False):
                    case True:
                        DataBase.DeleteDataObject(
                            Application.SelectedDataBaseItem)
                        os.system('cls||clear')
                    case False:
                        pass

            case 4:
                os.system('cls||clear')
                Application.ShowData()
            case 5:
                os.system('cls||clear')
                Application.MainMenu()

        Application.SelectedDataBaseItem = -1

        DataBase.SaveData()
