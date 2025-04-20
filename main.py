import json
import os
import yaml
from address import get_unique_address 
from host import get_host_configs

BASE_DIR = "../settings/config"
ADDRESS_DIR = f"{BASE_DIR}/address/" 
HOST_DIR = f"{BASE_DIR}/host/" 


def read_config_yaml(target_dir: str):
    configs = []
    for dir in os.listdir(target_dir):
        file_name = target_dir + dir 
        with open(file_name, 'r') as f:
            data = yaml.safe_load(f)
            configs.append(data)
    return configs

def generate_data_source(env, address_configs, host_configs) -> None:
    data_source = {
        "folders": {},
        "connections": {},
        "connection-types": {}
    }
    file = f"{env}/data-source.json"
    for address_config in address_configs:
        for host_config in host_configs:
            if address_config.address_config_id == host_config.address_config_id:
                data_source["connections"][address_config.address_config_id] = {
                    "name": address_config.address_config_id,
                    "configuration": {
                        "host": address_config.end_point,
                        "port": address_config.port,
                        "database": host_config.db_name
                    }
                }
    with open(file, 'w', encoding='utf-8') as fp:
        json.dump(data_source, fp, ensure_ascii=False, indent=4)


def main():
    host_data = read_config_yaml(HOST_DIR)
    address_data = read_config_yaml(ADDRESS_DIR)
    
    host_configs = get_host_configs(host_data)

    target_envs = {"dev"}
    for target_env in target_envs:
        address_configs = get_unique_address(address_data, target_env)
        generate_data_source(target_env, address_configs, host_configs)


if __name__ == "__main__":
    main()
