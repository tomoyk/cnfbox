from item import os, user, network


class CnfBox(object):
    def __init__(self):
        self.os = os.Os()
        self.user = user.User()
        self.network = network.Network()

    def show(self):
        for k, v in self.__dict__.items():
            print(f'{k}:'.ljust(10) + f'{v}')

    def show_json(self):
        # ObjectをJsonへ変換
        def default_method(item):
            if isinstance(item, object) and hasattr(item, '__dict__'):
                return item.__dict__
            else:
                raise TypeError
        import json
        print(json.dumps(self.__dict__, default=default_method, indent=4))

    def commit(self, parameter_list):
        pass
