import item.base


class Os(item.base.Base):
    __NAME_LIST: tuple = ('centos', 'ubuntu', 'debian')

    def __init__(
            self,
            name: str = 'ubuntu',
            version: float = 18.04,
            lang: str = 'jp',
            timezone: str = 'Asia/Tokyo'):
        assert name in Os.__NAME_LIST, f'"{name}" is not supported.'
        self.name = name
        self.version = version
        self.lang = lang
        self.timezone = timezone

    def __repr__(self):
        return f'{self.name} {str(self.version)}'
