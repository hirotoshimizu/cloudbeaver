from dataclasses import dataclass

@dataclass
class Address:
    address_config_id: str
    port: int | None
    end_point: str


def check_unique_db(address: dict[str, str], registerd_db) -> bool:
    for db in registerd_db:
        if db == address:
            return False
    return True

def get_unique_address(address_data, environment:str):
    address_configs, registerd_db = [], []
    for data in address_data:
        for addresses in data:
            for env in addresses["envs"]:
                if env["env"] == environment:
                    port = addresses.get("port", None)
                    end_point = env["end_point"]
                    unique_db = check_unique_db({port: end_point}, registerd_db)
                    if not unique_db:
                        continue
                    registerd_db.append({port: end_point})
                    address_configs.append(
                        Address(
                            address_config_id=addresses["address_config_id"],
                            port=port,
                            end_point=end_point
                        ))
    return address_configs
