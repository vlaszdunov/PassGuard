from Database import DataBase
from AdditionalClass import Additional
from Password import Password
import cutie
import os


class Application:

    MainMenuButtons = ['Показать пароли', 'Экспортировать пароли',
                       'Сгенерировать пароль', 'Добавить запись', 'Выйти']
    """Кнопки в главном меню"""

    DataObjectMenuButtons = ['Изменить пароль', 'Изменить сайт',
                             'Изменить логин', 'Удалить', 'Назад', 'В главное меню']
    """Кнопки при открытой записи пароля"""

    DataListButton = ['', '─'*20, 'Назад']
    Items = []

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
        Application.SelectedMenuItem = cutie.select(
            Application.MainMenuButtons)

    def ShowData():
        if len(DataBase.Data) == 0:
            print('╭'+'─'.center(40, '─')+'╮')
            print('│'+' '.center(40, ' ')+'│')
            print('│'+'ЗАПИСИ ОТСУТСТВУЮТ'.center(40, ' ')+'│')
            print('│'+' '.center(40, ' ')+'│')
            print('╰'+'─'.center(40, '─')+'╯')
        else:
            Application.Items = []
            for item in DataBase.Data:
                Application.Items.append(item.Site+'     '+item.Login)

            print('')
            print('    Сайт'+'     '+'Логин')
            print('─'*40)
            Application.SelectedDataBaseItem = Additional.Select(
                Application.Items, Application.DataListButton, [0, 1])

    def ShowDataObject():
        Additional.CreateTable(DataBase.Data[Application.SelectedDataBaseItem])
