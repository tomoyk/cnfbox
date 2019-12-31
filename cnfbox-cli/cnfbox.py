from item import os, user, network


def _get_json(dat: object) -> object:
    """ ObjectをJsonへ変換 """
    def default_method(item):
        if isinstance(item, object) and hasattr(item, '__dict__'):
            return item.__dict__
        else:
            raise TypeError
    import json
    return json.dumps(dat, default=default_method, indent=4)


class CnfBox(object):
    def __init__(self):
        self.os = os.Os()
        self.user = user.User()
        self.network = network.Network()

    def show(self):
        for k, v in self.__dict__.items():
            print(f'{k}:'.ljust(10) + f'{v}')

    def show_json(self):
        print(_get_json(self.__dict__))

    def commit(self):
        """ Get REMOTE URL """
        import os
        REMOTE_URL = os.getenv('REMOTE_URL')
        assert REMOTE_URL is None, "Env Var 'REMOTE_URL' is not set."

        """ Build HTTP Request """
        from urllib import request
        import json
        payload = _get_json(self.__dict__)
        req_body = json.dumps(payload).encode('utf-8')
        req_method = 'POST'
        req_headers = {
            'Content-Type': 'application/json',
        }
        req = request.Request(
            REMOTE_URL,
            data=req_body,
            method=req_method,
            headers=req_headers)
        try:
            with request.urlopen(req) as res:
                res_body = res.read().decode('utf-8')
                print(res_body)
        except Exception as e:
            print(e)
