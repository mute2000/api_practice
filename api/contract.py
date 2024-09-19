import requests

class ContractApi:
    def __init__(self):
        self.contract_url = "https://kdtx-test.itheima.net/api/common/upload"
        self.add_contract_url = "https://kdtx-test.itheima.net/api/contract"

    def upload_contract(self, contract_data, token):
        return requests.post(url=self.contract_url, files={"file": contract_data}, headers={"Authorization": token})
    
    def add_contract(self, add_contract_data, token):
        return requests.post(url=self.add_contract_url, json=add_contract_data, headers={"Authorization": token})
    
