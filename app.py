import pymongo
from helps import get_response, store
from spiders import get_courses

if __name__ == '__main__':
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['anu']
    collection = db['courses']

    count = 0
    for item in get_courses():
        store(item, collection)
        count += 1

    print(f'Total count: {count}')