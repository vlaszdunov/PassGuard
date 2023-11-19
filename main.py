from Password import Password
from Database import DataBase
from Application import Application
import cutie
import os
import json
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
                case False:
                    pass
            os.system('cls||clear')
        case 3:
            os.system('cls||clear')
            NewSite = input('Адрес сайта: ',)
            NewLogin = input('Логин/почта: ',)
            DataBase.CreateDataObject(NewLogin, NewSite)
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
                object_attributes = []
                DataBase.Data['Data'][Application.SelectedDataBaseItem] = Password(DataBase.Data['Data'][Application.SelectedMenuItem]['Id'], Password._generate_password(), DataBase.Data[
                                                                           'Data'][Application.SelectedMenuItem]['Login'], DataBase.Data['Data'][Application.SelectedMenuItem]['Site'], DataBase.Data['Data'][Application.SelectedMenuItem]['Comment']).__dict__
                print('Новый пароль: ',DataBase.Data['Data'][Application.SelectedDataBaseItem]['Password'])
                file = open(DataBase.FilePath, 'w')
                file.write(json.dumps(DataBase.Data))
                file.close()
                os.system('cls||clear')

            case 4:
                match cutie.prompt_yes_or_no('Удалить запись?', yes_text='Да, удалить', no_text='Нет, оставить', enter_empty_confirms=False, char_prompt=False):
                    case True:
                        DataBase.DeleteDataObject(
                            Application.SelectedDataBaseItem)
                        Application.SelectedDataBaseItem = -1
                        os.system('cls||clear')
                    case False:
                        pass
