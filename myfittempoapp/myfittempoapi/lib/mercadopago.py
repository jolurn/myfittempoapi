import requests
import json

class MercadoPago():

  PREDERENCE_URL = "https://api.mercadopago.com/checkout/preferences"
  
  def __init__(self, access_token):
    self.access_token = access_token

  def get_headers(self):
    HEADERS ={"Authorization": f"Bearer {self.access_token}"}
    return HEADERS

  def create_preference(self, data):
    dumpd_data = json.dumps(data)
    response = requests.request("POST", self.__class__.PREDERENCE_URL, data=dumpd_data, headers=self.get_headers())
    return response.json()