import json
import os
import requests


AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/'
REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
IMAGE_PATH = os.path.join(os.getcwd(), 'logo.png')

headers = {
    'Content-Type': 'application/json',
}

data = {
    'username': 'nocte',
    'password': '1q2w3e4r',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)

BASE_ENDPOINT = 'http://127.0.0.1:8000/api/status/'
EXTENDED_ENDPOINT = BASE_ENDPOINT + '12/'

headers2 = {
    # 'Content-Type': 'application/json',
    'Authorization': 'JWT ' + token,
}

data2 = {
    'content': 'this new content post'
}

# with open(IMAGE_PATH, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     r = requests.post(BASE_ENDPOINT, data=data2,
#                       headers=headers2, files=file_data)
#     print(r.text)

r = requests.get(EXTENDED_ENDPOINT, data=data2,
                 headers=headers2)
print(r.text)

# =============================================================

# AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/register/'
# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
# ENDPOINT = 'http://127.0.0.1:8000/api/status/'
# IMAGE_PATH = os.path.join(os.getcwd(), 'logo.png')

# headers = {
#     'Content-Type': 'application/json',
# }

# data = {
#     'username': 'nocte15',
#     'email': 'testuser15@gmail.com',
#     'password': '1q2w3e4r',
#     'password2': '1q2w3e4r'
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()  # cookies, expiration
# print(token)

# =============================================================

# AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/'
# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
# ENDPOINT = 'http://127.0.0.1:8000/api/status/'
# IMAGE_PATH = os.path.join(os.getcwd(), 'logo.png')

# data = {
#     'username': 'nocte',
#     'password': '1q2w3e4r'
# }

# headers = {
#     'Content-Type': 'application/json',
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()  # cookies, expiration
# print(token)


# =============================================================

# AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'
# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
# ENDPOINT = 'http://127.0.0.1:8000/api/status/'
# IMAGE_PATH = os.path.join(os.getcwd(), 'logo.png')

# data = {
#     'username': 'nocte',
#     'password': '1q2w3e4r'
# }

# headers = {
#     'Content-Type': 'application/json'
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()['token']  # cookies, expiration
# print(token)

# # Refresh
# refresh_data = {
#     'token': token
# }

# new_response = requests.post(
#     REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()  # ['token']
# print(new_token)

# # Change image and text
# headers = {
#     # 'Content-Type': 'application/json',
#     'Authorization': 'JWT ' + token,
# }

# with open(IMAGE_PATH, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {
#         'content': 'Updated description'
#     }

#     posted_response = requests.put(
#         ENDPOINT + str(20) + '/', data=data, headers=headers, files=file_data)
#     print(posted_response.text)

# # Only change text - DRF allows not setting the content type header
# headers = {
#     # 'Content-Type': 'application/json',
#     'Authorization': 'JWT ' + token,
# }

# data = {
#     'content': 'Updated description'
# }
# json_data = json.dumps(data)

# posted_response = requests.put(
#     ENDPOINT + str(20) + '/', data=json_data, headers=headers)
# print(posted_response.text)


# =============================================================
# ENDPOINT = 'http://127.0.0.1:8000/api/status/'

# get_endpoint = ENDPOINT + str(12)
# post_data = json.dumps({'content': 'Some random content'})

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers = {
#     'content-type': 'application/json'
# }
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)

# =============================================================
# ENDPOINT = 'http://127.0.0.1:8000/api/status/'
# IMAGE_PATH = os.path.join(os.getcwd(), 'logo.png')

# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     return r


# def do_img(method='post', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)

#     if img_path is not None:
#         with open(img_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data,
#                                  headers=headers, files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     return r


# # do_img(method='post', data={'user': 1, 'content': ''},
# #        is_json=False, img_path=IMAGE_PATH)

# do_img(method='put', data={'id': 12, 'user': 1, 'content': 'some new great content'},
#        is_json=False, img_path=IMAGE_PATH)

# # do(data={'id': 9})
# # do(method='delete', data={'id': 500})
# # do(method='put', data={'id': 9, 'content': 'some cool new content', 'user': 1})
# # do(method='post', data={'content': 'some cool new content', 'user': 1})
