import requests

BASE_URL = 'https://petstore.swagger.io/v2'

headers = {
    'accept': 'application/json',
    'api_key': 'Test'
}

json_for_post_request = {
                            'id': 9,
                            'category': {
                                 'id': 1,
                                 'name': 'cat'
                             },
                            'name': 'Tom',
                            'photoUrls': [
                                'string'
                              ],
                            'tags': [
                                {
                                  'id': 1,
                                  'name': 'T'
                                }
                              ],
                            'status': 'available'
                         }

post_response = requests.post(url=f"{BASE_URL}/pet",
                              json=json_for_post_request)

get_response = requests.get(url=f"{BASE_URL}/pet/9")

put_response = requests.put(url=f"{BASE_URL}/pet",
                            json={
                             'id': 9,
                             'category': {
                                 'id': 2,
                                 'name': 'dogs'
                             },
                             'name': 'Tommy',
                            "photoUrls": [
                                "url"
                              ],
                            "tags": [
                                {
                                  "id": 5,
                                  "name": "Tag"
                                }
                                ],
                            "status": "sold"
                            }
                            )

delete_response = requests.delete(url=f"{BASE_URL}/pet/9",
                                  headers=headers
                                  )
