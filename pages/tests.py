from django.test import TestCase
from .models import Message

class MessageTestCase(TestCase):
    def setUp(self):
        Message.objects.create(msg="Hi",priority=1)
        # Message.objects.create(msg="Hello",priority=1)
    def test_msg(self):
        user1 = Message.objects.get(id=1)
        expected_object_name = f'{user1.msg}'
        self.assertEqual(expected_object_name, 'Hi')
