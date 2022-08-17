import requests
from .exceptions import BitlyApiNotWorking, BitlyException

__version__ = "1.0.1"
bitli_api = "https://api.ksprojects.me/bitly?url={}"


def shorten_url(url: str) -> str:
    try:
        response = requests.get(bitli_api.format(url)).json()
    except Exception:
        raise BitlyApiNotWorking
    if response['success'] is True:
        return response.get('link')
    if response.get('message'):
        raise BitlyException(response['message'])
    raise BitlyApiNotWorking