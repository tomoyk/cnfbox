import item.base


def _validate_ip_format(ipaddr: str) -> str:
    ip_split = ipaddr.split('.')
    assert len(ip_split) == 4, "Invalid IP format."
    for ip in ip_split:
        assert 0 <= int(ip) <= 255, "Invalid IP range."
    return ipaddr


def _validate_cidr_range(cidr: int) -> int:
    assert 0 <= cidr <= 32, "Invalid Cidr range."
    return cidr


def _validate_iptype_format(type_: str) -> str:
    _ALLOW_TYPE = ('static', 'dhcp')
    assert type_ in _ALLOW_TYPE, f'Invalid IPtype. Allow type: {_ALLOW_TYPE}'
    return type_


class Network(item.base.Base):
    def __init__(
            self,
            device: str = 'eth0',
            iptype: str = 'static',
            ipaddr: str = '192.168.0.2',
            cidr: int = 24,
            gateway: str = '192.168.0.1',
            dns: str = '1.1.1.1',):
        self.device = device
        self.iptype = _validate_iptype_format(iptype)
        self.ipaddr = _validate_ip_format(ipaddr)
        self.cidr = _validate_cidr_range(cidr)
        self.gateway = _validate_ip_format(gateway)
        self.dns = _validate_ip_format(dns)

    def __repr__(self):
        return super().__repr__()
