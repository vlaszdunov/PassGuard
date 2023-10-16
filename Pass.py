import vars
import consts
if vars.AllowSpecSymbols == True:
    alphabet = consts.AlphabetWithSpecs
else:
    alphabet = consts.Alphabet


class Pass:

    Id = 0
    Login = ''
    Value = ''
    Site = ''
    Comment = ''

    def __init__(self, id: int, password: str, login: str, site: str, comment: str):
        self.Id = id
        self.Value = password
        self.Login = str(login)
        self.Site = str(site)
        self.Comment = str(comment)

    def _generate_password(self):
        NewPassword = ''
        for i in range(vars.PassLength):
            NewPassword += alphabet.pop()
            alphabet.add(NewPassword[-1])
        return NewPassword

    def ChangePassword(self):
        self.Value = ''
        for i in range(vars.PassLength):
            self.Value += alphabet.pop()
            alphabet.add(self.Value[-1])

    def ChangeLogin(self, login: str):
        self.Login = login

    def ChangeSite(self, site: str):
        self.Site = site

    def ChangeComment(self, comment: str):
        self.Comment = comment
