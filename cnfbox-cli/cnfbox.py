class CnfBox(object):
    _os_name: str = "ubuntu"
    _os_version: float = 18.04
    _username: str = 'admin'
    _password: str = None
    lang: str
    network: object

    @property
    def os(self):
        return f'{self._os_name} {str(self._os_version)}'

    @property
    def user(self):
        return f'{self._username}'

    @property
    def password(self):
        return f'{self._password}'

    def _get_random_txt(self, n: int = 12):
        assert n >= 12, "Need to set long password length."
        import random
        import string
        randlst = [random.choice(string.ascii_letters + string.digits)
                   for i in range(n)]
        return ''.join(randlst)

    def __init__(self):
        self._password = self._get_random_txt()

    def show(self):
        pass

    def check(self, parameter_list):
        pass

    def commit(self, parameter_list):
        pass
