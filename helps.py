import requests
from json.decoder import JSONDecodeError
from urllib.parse import urljoin, urlencode

def get_response(url, params, format='text'):
    """Fetches response of request for an URL by GET method

    Args:
        url: A http/https URL without parameters
        params: A dict containing parameters of request
        format: A string marking the format of result of this function

    Returns:
        Result of this request, of which format is marked by parameter format
        If request is forbidden, None

    Raises:
        ConnectError: request fails
        JSONDecodeError: failed parsing response into json
    """

    url = urljoin(url, '?' + urlencode(params))
    try: 
        resp = requests.get(url)

        if resp.status_code != 200:
            # Request fails
            return None
    except ConnectionError:
        return None

    if format == 'binary':
        return resp.content
    elif format == 'json':
        try:
            json = resp.json()
            return json
        except JSONDecodeError:
            return None
    else:
        return resp.text

def store(item, collection):
    collection.insert_one(item)
    print(f'Stored course {item["code"]}')