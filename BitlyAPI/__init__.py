import requests
from typing import List

from .model import Response
from .exceptions import BitlyApiNotWorking, BitlyException

__version__ = "1.0.3"
bitly_api = "https://api.ksprojects.me/bitly"


def shorten_urls(urls: List[str]) -> List[Response]:
    
    try:
        response = requests.post(bitly_api, json={"urls": urls}).json()
    except Exception:
        raise BitlyApiNotWorking
    if response.get('success') is False:
        raise BitlyException(response.get('message', 'error'))
    responses = []
    for d in response.get('data'):
        responses.append(
            Response('success', d.get('long_url'), d.get('short_url'))
        )
    for e in response.get('errors'):
        responses.append(
            Response(e.get('status_txt'), e['data'].get('long_url'), None)
        )
    if responses:
        return responses
    raise BitlyApiNotWorking