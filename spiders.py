import os
from helps import get_response

def get_courses():
    params = {
        'ShowAll': 'true',
        'Careers%5B0%5D': 'Undergraduate'
    }

    url = os.getenv('SEARCH_URL')

    # Fetching response
    print(f'Fetching response from {url}.....')
    json = get_response(url, params=params, format='json')

    if json == None:
        # Failed getting response
        print(f'Failed in fetching responses from {url}')
        return None

    # Finied fetching response
    print(f'Fetched response from {url}')

    for item in json.get('Items'):
        print(f'Yielded course: {item.get("CourseCode")}')
        yield {
            'code': item.get('CourseCode'),
            'name': item.get('Name'),
            'session': item.get('Session'),
            'units': item.get('Units')
        }

    

    