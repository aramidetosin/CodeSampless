import os
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print


script_dir = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(config_file=f"{script_dir}/config.yml")

response = nr.run(
    napalm_get,
    getters=['get_facts'])

print_result(response)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    device = {}
    data = response[dev].result['get_facts']
    hostname = data['fqdn']
    device[hostname] = {}
    device[hostname]['model'] = data['model']
    device[hostname]['uptime'] = data['uptime']
    device[hostname]['vendor'] = data['vendor']
    device[hostname]['version'] = data['os_version']
    devices.append(device)

print(devices)