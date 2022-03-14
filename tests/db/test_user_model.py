from django.test import TestCase

from db.models.user_model import User
from utils import Util


# Create your test(s) here.
class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            email="john.wick@gmail.com",
            password="password#3",
            username="WcKd",
            first_name="John",
            last_name="Wick",
            phone_number="2348093984569",
            address="7, Broad Street, Lagos-Island, Lagos",
            otp_code=Util.generate_otp()
        )

    def setUp(self):
        self.user = User.objects.get(email="john.wick@gmail.com")

    def test_get_username(self):
        username = self.user.get_username()
        self.assertEqual(username, "WcKd")

    def test_get_full_name(self):
        full_name = self.user.get_full_name()
        self.assertEqual(full_name, "John Wick")

    def test_get_short_name(self):
        short_name = self.user.get_short_name()
        self.assertEqual(short_name, "John")

    def test_get_phone_number(self):
        phone_number = self.user.get_phone_number()
        self.assertEqual(phone_number, "2348093984569")

    def test_get_address(self):
        address = self.user.get_address()
        self.assertEqual(address, "7, Broad Street, Lagos-Island, Lagos")

    def test_email_label(self):
        email_label = self.user._meta.get_field("email").verbose_name
        self.assertEqual(email_label, "email address")
