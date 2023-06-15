from flask import Flask
from flask_restful import Api
from resources import MenuResource, PaymentResource, TippingResource, NotificationResource

app = Flask(__name__)
api = Api(app)

api.add_resource(MenuResource, '/menu')
api.add_resource(PaymentResource, '/payment')
api.add_resource(TippingResource, '/tip')
api.add_resource(NotificationResource, '/notification')

if __name__ == '__main__':
    app.run(debug=True)