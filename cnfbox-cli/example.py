from cnfbox import CnfBox

cb = CnfBox()

cb.os.name = 'centos'
cb.os.version = 8.0
cb.os.lang = 'us'
cb.os.keyboard = 'jp'
cb.os.timezone = 'Asia/Tokyo'

cb.user = ['alice', 'bob']

cb.network.device = 'ens160'
cb.network.iptype = 'static'
cb.network.ipaddr = '10.200.1.5'
cb.network.cidr = 16
cb.network.gateway = '10.200.1.254'
cb.network.dns = '10.200.1.3'

cb.storage.bootloader = 'mbr'
cb.storage.auto_partition = True
cb.storage.clear_partition = True

cb.show()
cb.commit()
