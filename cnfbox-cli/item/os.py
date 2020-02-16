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
        assert language_supported in Os.__COUNTRY_LIST, f'"{lang}" is not in acceptable language.'
        assert keyboard_layout in Os.__COUNTRY_LIST, f'{keyboard} is not in acceptable language.'
        self.name = name
        self.version = version
        self.language_supported = language_supported
        self.timezone = timezone
        self.keyboard_layout = keyboard_layout

    def __repr__(self):
        return super().__repr__()
