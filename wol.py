from wakeonlan import wol
import requests
import logging
import yaml
import time
import os

logger = logging.getLogger('wol')

cwd = os.path.dirname(os.path.abspath(__file__))
try:
    conf = yaml.safe_load(open(cwd + '/config.yml'))
except IOError:
    logger.error('Can\'t find file config.yml')

target_servers = conf['servers']

resp = requests.get(conf['census_url'])

for server in resp.json()['servers']:
    if server['hostname'] in target_servers.keys() and not server['isOk']:
        logger.info("%s is down, sending WOL" % server['hostname'])
        wol.send_magic_packet(target_servers[server['hostname']])
        time.sleep(10)
