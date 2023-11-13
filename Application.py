from Password import Password
from Database import DataBase
import cutie


class Application:
    
    MainMenuButtons = ['Показать пароли', 'Экспортировать пароли',
                       'Создать пароль', 'Добавить запись']
    """Кнопки в главном меню"""
    PasswordMEnuButtons = ['Изменить пароль', 'Изменить сайт',
                           'Изменить логин', 'Изменить комментарий', 'Удалить', 'Назад']
    """Кнопки при открытой записи пароля"""

    MenuItems = []
    """Список записей в главном меню"""

    SelectedItem = 0
    
    def __init__(self, database) -> None:
        print('╭'+'─'.center(60, '─')+'╮')
        print('│'+' '.center(60, ' ')+'│')
        print('│'+'PassGuard'.center(60, ' ')+'│')
        print('│'+' '.center(60, ' ')+'│')
        print('│'+'Консольный менеджер паролей'.center(60, ' ')+'│')
        print('│'+'Храните и генерируйте случайные пароли'.center(60, ' ')+'│')
        print('│'+' '.center(60, ' ')+'│')
        print('╰'+'─'.center(60, '─')+'╯')
        print('')
        print('Главное меню')
        print('─'.center(30, '─'))

        for i in database.Data['Data']:
            if len(i['Site']) < database.MaxSiteLen:
                self.MenuItems.append(
                    i['Site']+' '*(database.MaxSiteLen-len(i['Site']))+'     '+i['Login'])
            else:
                self.MenuItems.append(i['Site']+'     '+i['Login'])

    def MainMenu(self, database):
        match cutie.select(Application.MainMenuButtons):
            case 0:
                print('')
                print('Сайты и логины, для которых сохранен пароль')
                print('Сайт'+" "*(database.MaxSiteLen)+'     '+'Логин')
                print('───────────────────────────────────────────')
                self.SelectedItem = cutie.select(self.MenuItems)
                return 

    def ShowDatabaseItem(self, database):
        print('')
        print('Сайт:  ',database.Data['Data'][self.SelectedItem]['Site'])
        print('Логин: ',database.Data['Data'][self.SelectedItem]['Login'])
        print('Пароль:',database.Data['Data'][self.SelectedItem]['Value'])
        print('')
        match cutie.select(Application.PasswordMEnuButtons):
            case 0:
               return Password._generate_password() 
            case 5:
                for i in range(20):
                    print(' ')
                return 
                
