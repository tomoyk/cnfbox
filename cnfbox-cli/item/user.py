import item.base


class User(item.base.Base):
    def __init__(self, users: list = ["admin"]):
        self.name = users
        self.password = {u: self._get_random_txt() for u in users}

    def __repr__(self):
        return str(self.password)

    def _get_random_txt(self, n: int = 12):
        assert n >= 12, "Need to set long password length."
        import random
        import string
        randlst = [random.choice(string.ascii_letters + string.digits)
                   for i in range(n)]
        return ''.join(randlst)

    @property
    def user(self):
        return self.name

    @user.setter
    def user(self, users):
        self.name = users
        self.password = {u: self._get_random_txt() for u in users}

    @user.deleter
    def user(self):
        self.name = []
        self.password = {}

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self):
        pass

    @password.deleter
    def password(self):
        pass