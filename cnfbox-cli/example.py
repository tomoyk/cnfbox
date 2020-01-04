from cnfbox import CnfBox

cb = CnfBox()

cb.os.name = 'centos'
cb.os.version = 8.0
cb.os.lang = 'us'

cb.user = ['alice', 'bob']

cb.network.device = 'ens160'
cb.network.iptype = 'static'
cb.network.ipaddr = '10.200.1.5'
cb.network.cidr = 16
cb.network.gateway = '10.200.1.254'
cb.network.dns = '10.200.1.3'

print(cb.show_json())
