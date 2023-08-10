import requests
import json
from config import keys_ap

class PrognozException(Exception):
    pass

class Match:
    @staticmethod
    def resalt(match: str):

        match_ticker = keys_ap[match]

        return match_ticker