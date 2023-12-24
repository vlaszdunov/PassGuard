from ProgramData.Database import DataBase
from ProgramData.AdditionalClass import Additional
from ProgramData.Password import Password
import cutie
import os


class Application:

    MainMenuButtons = ['Показать пароли', 'Экспортировать пароли',
                       'Сгенерировать пароль', 'Добавить запись', 'Выйти']
    """Кнопки в главном меню"""

    DataObjectMenuButtons = ['Изменить пароль', 'Изменить сайт',
                             'Изменить логин', 'Удалить', 'Назад', 'В главное меню']
    """Кнопки при открытой записи пароля"""

    DataListButton = ['', '─'*20, 'В главное меню']
    MaxSiteLen = 0
    Items = []
    SelectedDataBaseItem = -1
    SelectedMenuItem = -1
    Return = False

    @staticmethod
    def __init__() -> None:
        os.system('cls||clear')
        print('╭'+'─'.center(60, '─')+'╮')
        print('│'+' '.center(60, ' ')+'│')
        print('│'+'PassGuard'.center(60, ' ')+'│')
        print('│'+' '.center(60, ' ')+'│')
        print('│'+'Консольный менеджер паролей'.center(60, ' ')+'│')
        print('│'+'Разработал Здунов Влас. Группа 2021-ФГиИБ-ИСиТ-2б'.center(60, ' ')+'│')
        print('│'+' '.center(60, ' ')+'│')
        print('╰'+'─'.center(60, '─')+'╯')

    def MainMenu():
        print('')
        print('Главное меню')
        print('─'*30)
        Application.SelectedMenuItem = Additional.Select(
            Application.MainMenuButtons)

    def ShowData():
        os.system('cls||clear')
        if len(DataBase.Data) == 0:
            print('╭'+'─'.center(40, '─')+'╮')
            print('│'+' '.center(40, ' ')+'│')
            print('│'+'ЗАПИСИ ОТСУТСТВУЮТ'.center(40, ' ')+'│')
            print('│'+' '.center(40, ' ')+'│')
            print('╰'+'─'.center(40, '─')+'╯')
        else:
            Application.SelectedDataBaseItem = -1
            for Row in DataBase.Data:
                if len(Row.Site) > Application.MaxSiteLen:
                    Application.MaxSiteLen = len(Row.Site)
            Application.Items = []
            for item in DataBase.Data:
                Application.Items.append(
                    item.Site+' '*(Application.MaxSiteLen-len(item.Site))+'     '+item.Login)

            print('    Сайт'+' '*(Application.MaxSiteLen-4)+'     '+'Логин')
            print('─'*40)
            Application.SelectedDataBaseItem = Additional.Select(
                Application.Items, Application.DataListButton, [0, 1])

    def ShowDataObject():
        os.system('cls||clear')
        Additional.CreateTable(DataBase.Data[Application.SelectedDataBaseItem])

    def ExportData():
        DataBase.ExportData()
        os.system('cls||clear')
        print('╭'+'─'.center(40, '─')+'╮')
        print('│'+' '.center(40, ' ')+'│')
        print('│'+'Экспортировано в Загрузки'.center(40, ' ')+'│')
        print('│'+' '.center(40, ' ')+'│')
        print('╰'+'─'.center(40, '─')+'╯')
