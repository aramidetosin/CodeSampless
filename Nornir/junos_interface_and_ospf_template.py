from nornir_pyez.plugins.tasks import pyez_config, pyez_diff, pyez_commit
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
import os
from pprint import pprint as pp
from nornir_utils.plugins.tasks.data import load_yaml


script_dir = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(config_file=f"{script_dir}/config.yml")

junos_devices = nr.filter(F(node_type="router"))


def int_config(task):
    data = {}
    data['interfaces'] = {}


    for intf in task.host['interfaces']:
        data['interfaces'][intf] = {}
        for add in task.host['interfaces'][intf]:
            data['interfaces'][intf]['ipv4_address'] = task.host['interfaces'][intf][add]
    int_response = task.run(name='int config', task=pyez_config,
                            template_path='/Users/aramide/PycharmProjects/CodeSamples/Nornir/templates/junos'
                                          '/interfaces.j2',
                            template_vars=data, data_format='xml')

    if int_response:
        diff = task.run(task=pyez_diff, name='int diff')
    if diff:
        commit = task.run(task=pyez_commit, name='int commit')


def ospf_config(task):
    data = {}
    # data['ospf_area'] = task.host['ospf_area']
    # data['ospf_int_1'] = task.host['ospf_int_1']
    data['ospf_int_1'] = {}

    ospf_interfaces = task.host['ospf_int_1']

    for area, int in ospf_interfaces.items():

        intf_list = []
        for i in int:
            intf_list.append(i)
        data['ospf_int_1'][area] = intf_list

    # print(data)
    response = task.run(task=pyez_config, template_path='/Users/aramide/PycharmProjects/CodeSamples/Nornir/templates'
                                                        '/junos/ospf.j2',
                        template_vars=data, data_format='xml', name='config ospf')
    print(response.result)
    if response:
        diff = task.run(pyez_diff)
    if diff:
        commit = task.run(pyez_commit)



send_result = junos_devices.run(
    task=int_config)
print_result(send_result)

ospf_result = junos_devices.run(
    task=ospf_config)
print_result(ospf_result)
