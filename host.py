from dataclasses import dataclass


@dataclass
class Host:
    host_config_id: str
    address_config_id: str
    db_name: str


def get_host_configs(host_data):
    host_configs = []
    for data in host_data:
        for host in data:
            host_configs.append(
                Host(
                    host_config_id=host["host_config_id"],
                    address_config_id=host["address_config_id"],
                    db_name=host["db_name"]
                ))
    return host_configs
