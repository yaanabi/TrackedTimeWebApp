from dotenv import load_dotenv, find_dotenv
from os import environ
load_dotenv(find_dotenv())


MONGODB_URL = environ['MONGODB_URL']
MONGODB_NAME = environ['MONGODB_NAME']