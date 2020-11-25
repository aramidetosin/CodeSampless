from scrapli.driver.core import IOSXEDriver
from ttp import ttp

my_device = {
    "host": "192.168.20.135",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
}
ttp_template = """interface {{ interface }}
 ip address {{ ip }} {{ mask }}
 description {{ description }}"""

# with IOSXEDriver(**my_device) as conn:
#     response = conn.send_commands(["show run", "show ip int brief"])
#     print(response.result)

with IOSXEDriver(**my_device) as conn:
    response = conn.send_command("show run interface GigabitEthernet2")
    data_to_parse = response.result
    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()
    results = parser.result(format='json')[0]
    print(results)
    # structured_result = response.ttp_parse_output(template="my_template.ttp")
    # print(structured_result)