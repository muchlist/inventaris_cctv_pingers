import requests


class Postman(object):
    params_get = {}
    params_post = {}
    base_url = ""

    def __init__(self):
        self.params_get = {
            "key": "gulugulugulu",
            "branch": "BANJARMASIN"
        }
        self.params_post = {
            "key": "gulugulugulu"
        }
        self.base_url = "http://localhost:5001"

    def set_base_url(self, base_url: str):
        self.base_url = base_url

    def set_param_post(self, params: dict):
        self.params_post = params

    def set_param_get(self, params: dict):
        self.params_get = params

    def get_ip_list(self) -> list:
        url = f"{self.base_url}/api/cctv-ip"
        x = requests.get(url, params=self.params_get, timeout=2.50)
        if x.status_code == 200:
            json_response = x.json()
            return json_response["cctv_ip"]
        else:
            return []

    def post_ip_status(self, cctv_list: list, code: int) -> str:
        url = f"{self.base_url}/api/cctv-states-update"
        body = {
            "ip_addresses": cctv_list,
            "ping_code": code
        }
        x = requests.post(url, json=body, params=self.params_post)
        if x.status_code == 200:
            return x.text
        else:
            return "Error"
