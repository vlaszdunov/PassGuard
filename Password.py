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
        Value (str): Пароль пользователя
        Site (str): URL-адрес сайта, для которого сохранятеся информация
        Comment (str): Комментарий к записи
    
    Methods:
        ChangePassword: some shit
    """

    Id = 0
    Login = ''
    Value = ''
    Site = ''
    Comment = ''

    def __init__(self, id: int, password: str, login: str, site: str, comment: str='—') -> None:

        self.Id = id
        self.Value = str(password)
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

    def ChangePassword(self) -> None:
        self.Value = ''
        for i in range(vars.PassLength):
            self.Value += alphabet.pop()
            alphabet.add(self.Value[-1])

    def ChangeLogin(self, log: str) -> None:
        self.Login = log

    def ChangeSite(self, site: str) -> None:
        self.Site = site

    def ChangeComment(self, comment: str) -> None:
        self.Comment = comment
