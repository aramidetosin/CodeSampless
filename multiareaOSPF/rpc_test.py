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
# extras = {
#     "level-extra": "terse",
#     "interface-name": "ge-0/0/0"
# }

extras = {
    "level-extra": "brief",
    "neighbor": "192.168.34.3"
}

response = nr.run(
    task=pyez_rpc, func='get-ospf-neighbor-information', extras=None
)
# response = nr.run(
#     task=pyez_rpc, func='get-interface-information', extras=extras)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)