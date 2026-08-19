import os
from dotenv import load_dotenv

load_dotenv()


def ipstackapi():
    return os.getenv("IPSTACK_API_KEY")


def macvendor():
    return os.getenv("MACVENDORS_API_KEY")


def phoneapis():
    return os.getenv("PHONE_API_KEY")
