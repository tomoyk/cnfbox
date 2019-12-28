from item import os, user


class CnfBox(object):
    _os: object
    _user: object

    @property
    def os(self):
        return self._os

    @property
    def user(self):
        return self._user

    def __init__(self):
        self._os = os.Os()
        self._user = user.User()

    def show(self):
        pass

    def check(self, parameter_list):
        pass

    def commit(self, parameter_list):
        pass
