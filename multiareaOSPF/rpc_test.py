from nornir_pyez.plugins.tasks import pyez_rpc
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print
from nornir.core.plugins.connections import ConnectionPluginRegister
from nornir_pyez.plugins.connections import Pyez


ConnectionPluginRegister.register("pyez", Pyez)


script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")

# xpath = 'interfaces/interface'
# xml = '<interfaces></interfaces>'
# database = 'committed'
extras = {
    "level-extra": "terse",
    "interface-name": "fxp0"
}

# extras = {
    # "level-extra": "brief",
    # "neighbor": "192.168.34.3"
# }

# response = nr.run(
    # task=pyez_rpc, func='get-ospf-neighbor-information', extras=None
# )
response = nr.run(
    task=pyez_rpc, func='get-interface-information', extras=extras)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
# print_result(response)
for dev in response:
    print(dev)
    print(response[dev].result['interface-information']['physical-interface']['logical-interface'])
    # print(dev)
#     # for i in response[dev].result['ospf-neighbor-information']['ospf-neighbor']:
#     #     print(i['neighbor-id'])
    # print(f"{dev}: Interface ge-0/0/0 is oper-status [red]{response[dev].result['interface-information']['physical-interface']['logical-interface']['oper-status']}[/red]")