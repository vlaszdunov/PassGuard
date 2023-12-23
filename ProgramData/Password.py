import consts
import vars
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

    Methods:
        ChangePassword: some shit
    """

    Id = 0
    Site = ''
    Login = ''
    Password = ''

    def __init__(self, id: int, site: str, login: str, password: str = None) -> None:
        self.Id = id
        self.Site = str(site)
        self.Login = str(login)
        if password==None:
            self.Password = Password._generate_password()
        else:
            self.Password = str(password)


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


