class User(object):
    _name: list
    _password: dict

    def __init__(self, users: list = ["admin"]):
        self._name = users
        self._password = {u: self._get_random_txt() for u in users}

    def __repr__(self):
        return str(self._password)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._password = {u: self._get_random_txt() for u in value}

    @property
    def password(self):
        return [str(p) for p in self._password.values()]

    def _get_random_txt(self, n: int = 12):
        assert n >= 12, "Need to set long password length."
        import random
        import string
        randlst = [random.choice(string.ascii_letters + string.digits)
                   for i in range(n)]
        return ''.join(randlst)
