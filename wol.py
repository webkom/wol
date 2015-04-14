from wakeonlan import wol
import requests
import logging
import yaml
import time

conf = yaml.safe_load(open('config.yml'))

target_servers = conf['servers']

logger = logging.getLogger('wol')

resp = requests.get(conf['census_url'])

for server in resp.json()['servers']:
    if server['hostname'] in target_servers.keys() and not server['isOk']:
        print("%s is down, sending WOL" % server['hostname'])
        wol.send_magic_packet(target_servers[server['hostname']])
        time.sleep(10)
