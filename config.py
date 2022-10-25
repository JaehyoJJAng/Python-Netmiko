import json
from pathlib import Path
from typing import Optional
import os
class GetIP:
    BASE_DIR  = Path(__file__).resolve().parent
    JSON_FILE = os.path.join(BASE_DIR,'ip.json')

    @classmethod
    def get_ip(
            cls,
            key: str,
            default_value: Optional[str] = None,
    ):
        with open(cls.JSON_FILE,'r',encoding='UTF-8') as file:
            ips = json.loads(file.read())

            try:
                return ips[key]
            except KeyError:
                if default_value:
                    return default_value
                raise EnvironmentError(f'Set the {key} environment variable')
get_ip = GetIP()
