import requests  # http requests
import json

BASE_URL = 'http://127.0.0.1:8000/'

ENDPOINT = 'api/updates/'


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 404:  # [Page] Not Found
        print("probably a good sign?")
    elif status_code != 200:
        print("probably not a good sign?")

    data = r.json()
    # print(type(json.dumps(data)))
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            # print(dir(r2))
            print(r2.json())

    return data


def create_update():
    new_data = {
        'user': 1,
        'content': 'Some cooler content update'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def delete_update():
    new_data = {
        'user': 1,
        'content': 'Another new cool update'
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def do_obj_update():
    new_data = {
        'content': 'New obj data'
    }
    r = requests.put(BASE_URL + ENDPOINT + '1/', data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def do_obj_delete():
    r = requests.delete(BASE_URL + ENDPOINT + '1/')
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


# print(get_list())
print(create_update())
# print(delete_update())
# print(do_obj_update())
# print(do_obj_delete())
