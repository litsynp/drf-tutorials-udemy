import json
import os
import requests

ENDPOINT = 'http://127.0.0.1:8000/api/status/'
IMAGE_PATH = os.path.join(os.getcwd(), 'logo.png')


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
