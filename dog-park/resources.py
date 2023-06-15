from flask_restful import Resource

class MenuResource(Resource):
    def get(self):
        """
        Returns the menu of the dog park/coffee shop
        """
        pass

class PaymentResource(Resource):
    def post(self):
        """
        Processes the payment for the selected products/services
        """
        pass

class TippingResource(Resource):
    def post(self):
        """
        Processes the tip for the selected amount and payment method
        """
        pass

class NotificationResource(Resource):
    def post(self):
        """
        Sends a push notification to the user's device
        """
        pass