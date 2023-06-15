import squareconnect
from squareconnect.apis import locations_api, transactions_api
from squareconnect.models import ChargeRequest, Money

class PaymentGateway:
    def __init__(self, access_token, location_id):
        self.access_token = access_token
        self.location_id = location_id
        self.locations_api = locations_api.LocationsApi()
        self.transactions_api = transactions_api.TransactionsApi()
    
    def charge_card(self, card_data, amount):
        """
        Charges the provided card with the specified amount
        """
        pass