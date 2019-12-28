import item.base


class Network(item.base.Base):
    def __init__(
            self,
            device: str = 'eth0',
            iptype: str = 'static',
            ipaddr: str = '192.168.0.2',
            cidr: int = 24,
            gateway: str = '192.168.0.1',
            dns: str = '1.1.1.1',
    ):
        self.device = device
        self.type = iptype
        self.ipaddr = ipaddr
        self.cidr = cidr
        self.gateway = gateway
        self.dns = dns

    def __repr__(self):
        return super().__repr__()
