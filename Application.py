from Password import Password
from Database import DataBase
import cutie
import os

class Application:

    MainMenuButtons = ['Показать пароли', 'Экспортировать пароли',
                       'Сгенерировать пароль', 'Добавить запись', 'Выйти']
    """Кнопки в главном меню"""

    DataMenuButtons = ['Изменить пароль', 'Изменить сайт',
                           'Изменить логин', 'Изменить комментарий', 'Удалить', 'Назад']
    """Кнопки при открытой записи пароля"""

    SelectedMenuItem = 0
    SelectedDataBaseItem = -1
    Items = []

    @staticmethod
    def __init__() -> None:
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
        if len(DataBase.Data['Data'])==0:
            print('╭'+'─'.center(40, '─')+'╮')
            print('│'+' '.center(40, ' ')+'│')
            print('│'+'ЗАПИСИ ОТСУТСТВУЮТ'.center(40, ' ')+'│')
            print('│'+' '.center(40, ' ')+'│')
            print('╰'+'─'.center(40, '─')+'╯')
        else:
            Application.Items=[]
            for item in DataBase.Data['Data']:
                Application.Items.append(
                    item['Site']+' '*(DataBase.MaxSiteLen-len(item['Site']))+'     '+item['Login'])

            print('')
            print('    Сайт'+' '*(DataBase.MaxSiteLen-4)+'     '+'Логин')
            print('─'*40)
            Application.SelectedDataBaseItem = cutie.select(Application.Items)
    
    def ShowDataObject():
        Application.Items=['','','']
        for key in DataBase.Data['Data'][Application.SelectedDataBaseItem]:
            if key=='Site':
                if 4<len(DataBase.Data['Data'][Application.SelectedDataBaseItem][key]):
                    Application.Items[0]+=('Сайт'+' '*(len(DataBase.Data['Data'][Application.SelectedDataBaseItem][key])-4)+'     ')
            if key=='Login':
                if 5<len(DataBase.Data['Data'][Application.SelectedDataBaseItem][key]):
                    Application.Items[0]+=('Логин'+' '*(len(DataBase.Data['Data'][Application.SelectedDataBaseItem][key])-5)+'     ')
            if key=='Password':
                if 6<len(DataBase.Data['Data'][Application.SelectedDataBaseItem][key]):
                    Application.Items[0]+=('Пароль'+' '*(len(DataBase.Data['Data'][Application.SelectedDataBaseItem][key])-6)+'     ')
        Application.Items[1]='─'*len(Application.Items[0])
        for key in DataBase.Data['Data'][Application.SelectedDataBaseItem]:
            if key in ['Site','Login','Password']:
                Application.Items[2]+=((DataBase.Data['Data'][Application.SelectedDataBaseItem][key]+'     '))

        print('')
        for i in Application.Items:
            print(i,end='\n')
