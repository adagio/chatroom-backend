from django.test import TestCase

#import pytest
#from channels.testing import HttpCommunicator
from ..core.models import User, Message
# from ..channels_app import consumers
from ..channels_app.consumers import ChatConsumer
# from django.contrib.auth.models import User


class ChatTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('user1', password='userpass1')
        self.client.login(username='user1', password='userpass1')

    def test_fetch_messages(self):
        consumer = ChatConsumer()
        response = consumer.fetch_messages(data='')
        assert response["body"] == b"test response"
        assert response["status"] == 200

    def test_get_last_50_messages(self):
        messages = Message.last_50_messages()
        ml = len(messages)
        self.assertLessEqual(ml, 50)
