class Os(object):
    _name_list: tuple = ('centos', 'ubuntu', 'debian')
    _name: str
    _version: float

    def __init__(self, name: str = 'ubuntu', version: float = 18.04):
        assert name in self._name_list, f'"{name}" is not supported.'
        self._name = name
        self._version = version

    def __repr__(self):
        return f'{self._name} {str(self._version)}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert value in self._name_list, f'"{value}" is not supported.'
        self._name = value

    @property
    def version(self):
        return self._version
