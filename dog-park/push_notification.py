import firebase_admin
from firebase_admin import credentials, messaging

class PushNotification:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(self.cred)
    
    def send_notification(self, notification_data):
        """
        Sends a push notification to the user's device with the provided notification data
        """
        pass