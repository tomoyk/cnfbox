import item.base


class Os(item.base.Base):
    __NAME_LIST: tuple = ('centos', 'ubuntu', 'debian')
    __COUNTRY_LIST: tuple = ('us', 'jp')

    def __init__(
            self,
            name: str = 'ubuntu',
            version: float = 18.04,
            language_supported: str = 'jp',
            timezone: str = 'Asia/Tokyo',
            keyboard_layout: str = 'jp'):
        assert name in Os.__NAME_LIST, f'"{name}" is not supported.'
        assert lang in Os.__COUNTRY_LIST, f'"{lang}" is not in acceptable language.'
        assert keyboard in Os.__COUNTRY_LIST, f'{keyboard} is not in acceptable language.'
        self.name = name
        self.version = version
        self.lang = lang
        self.timezone = timezone
        self.keyboard = keyboard

    def __repr__(self):
        return super().__repr__()
