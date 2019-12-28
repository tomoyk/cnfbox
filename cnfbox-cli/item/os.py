class Os(object):
    _NAME_LIST: tuple = ('centos', 'ubuntu', 'debian')
    _name: str
    _version: float
    _lang: str
    _timezone: str

    def __init__(
            self,
            name: str = 'ubuntu',
            version: float = 18.04,
            lang: str = 'jp',
            timezone: str = 'Asia/Tokyo'):
        assert name in self._NAME_LIST, f'"{name}" is not supported.'
        self._name = name
        self._version = version
        self._lang = lang
        self._timezone = timezone

    def __repr__(self):
        return f'{self._name} {str(self._version)}'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        assert value in self._NAME_LIST, f'"{value}" is not supported.'
        self._name = value

    @property
    def version(self) -> float:
        return self._version

    @version.setter
    def version(self, value: float):
        self._version = value

    @property
    def lang(self) -> str:
        return self._lang

    @lang.setter
    def lang(self, value: str):
        self._lang = value

    @property
    def timezone(self) -> str:
        return self._timezone

    @timezone.setter
    def timezone(self, value: str):
        self._timezone = value
