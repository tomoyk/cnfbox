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

    def __init__(self):
        pass
    
    def show(self):
        pass

    def check(self, parameter_list):
        pass

    def commit(self, parameter_list):
        pass
