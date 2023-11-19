"""
Файл, хранящий класс Password
"""

import vars
import consts
if vars.AllowSpecSymbols == True:
    alphabet = consts.AlphabetWithSpecs
else:
    alphabet = consts.Alphabet


class Password:
    """Основной класс программы. Отвечает за работу с записями    


    Attributes:
        Id (int): Уникальный идентификатор записи
        Login (str): Логин, связанный с введенным паролем
        Password (str): Пароль пользователя
        Site (str): URL-адрес сайта, для которого сохранятеся информация
        Comment (str): Комментарий к записи
    
    Methods:
        ChangePassword: some shit
    """

    Id = 0
    Login = ''
    Password = ''
    Site = ''
    Comment = ''

    def __init__(self, id: int, password: str, login: str, site: str, comment: str='-') -> None:

        self.Id = id
        self.Password = str(password)
        self.Login = str(login)
        self.Site = str(site)
        self.Comment = str(comment)

    @staticmethod
    def _generate_password() -> str:
        """Статический метод, генерирующий пароль

        Returns:
            str: Сгенерированный пароль
        """
        NewPassword = ''
        for i in range(vars.PassLength):
            NewPassword += alphabet.pop()
            alphabet.add(NewPassword[-1])
        return NewPassword
