from item import os, user, network


class CnfBox(object):
    def __init__(self):
        self.os = os.Os()
        self.user = user.User()
        self.network = network.Network()

    def show(self):
        pass

    def check(self, parameter_list):
        pass

    def commit(self, parameter_list):
        pass
