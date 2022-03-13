import random


class Util:
    # Generate OTP
    @staticmethod
    def generate_otp():
        otp_code = random.randrange(100000, 1000000)
        return otp_code
