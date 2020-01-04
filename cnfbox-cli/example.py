from cnfbox import CnfBox
cb = CnfBox()
cb.os.name = 'centos'
cb.os.version = 8.0
cb.os.lang = 'us'
cb.user = ['alice', 'bob']
print(cb.show_json())
