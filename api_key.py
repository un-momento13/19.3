import requests
import json
base_url = 'https://petstore.swagger.io/v2'
# username = 'un-momento'
username = 'uno13'
headers={'accept': 'application/json', 'Content-Type': 'application/json'}

####  user: Operations about user  ####
print('**************************   user   **********************************')
res = requests.get(f"{base_url}/user/login", headers={'accept': 'application/json', 'username': username, 'password': '789456'})
print('\nЗапрос GET/user/login: Logs user into the system:', res.text, sep='\n')

res = requests.get(f"{base_url}/user/logout", headers={'accept':'application/json'})
print('\nЗапрос GET/user/logout: Logs out current logged in user session:', res.text, sep='\n')

data={
    'id': 11,
    'username': 'uno13',
    'firstname': 'string',
    'lastname': 'string',
    'email': 'uno-momento@yandex.ru',
    'password': '789456',
    'phone': '89648888888',
    'userStatus': 0
}

res = requests.post(f"{base_url}/user", headers=headers, json=data)
# j_data = json.dumps(data)
# res = requests.post(f"{base_url}/user", headers=headers, data=j_data)
print('\nЗапрос POST/user: Create user:', res.json(), sep='\n')

data_upd = {
    'id': 3,
    'username': 'uno13',
    'firstname': 'string',
    'lastname': 'string',
    'email': 'uno-momento@yandex.ru',
    'password': '789456',
    'phone': '89648888888',
    'userStatus': 0
}
res = requests.put(f"{base_url}/user/{username}", headers=headers, json=data_upd)
print('\nЗапрос PUT/user/{username}: Updated user:', res.json(), sep='\n')
# В информации "Updated user" по ключу 'message': '3' указывается число параметров, которые были изменены

res = requests.get(f"{base_url}/user/{username}", headers={'accept': 'application/json'})
print(f'\nЗапрос GET/user/{username}: Get user by username:', res.json(), sep='\n')

res = requests.delete(f"{base_url}/user/{username}", headers=headers)
print(f'\nЗапрос DEL/user/{username}: Delete user:', res.text, sep='\n')

array = [
  {
    "id": 1,
    "username": "Jon",
    "firstName": "Jon",
    "lastName": "Silver",
    "email": "j_silver@mail,ru",
    "password": "999",
    "phone": "131313",
    "userStatus": 0
  },
{
    "id": 2,
    "username": "Billy",
    "firstName": "Billy",
    "lastName": "Bons",
    "email": "b_bons@yandex.ru",
    "password": "666",
    "phone": "313131",
    "userStatus": 0
  },
]
res = requests.post(f"{base_url}/user/createWithArray", headers=headers, json=array)
print('\nЗапрос POST/user/createWithArray: Creates list of users with given input array:\n', res.status_code, res.json(), end='\n')

res = requests.post(f"{base_url}/user/createWithList", headers=headers, json=array)
print('\nЗапрос POST/user/createWithList: Creates list of users with given input array:\n', res.status_code, res.json(), end='\n\n')


### Pets: everything about pets ####
print('**************************   pets   **********************************')
petId = 1
data_pet_1 = {
  "id": 1,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Chucha",
  "photoUrls": [
    "photoUrls"
  ],
  "tags": [
    {
      "id": 1,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(f"{base_url}/pet", headers=headers, json=data_pet_1)
print(f'Запрос POST/pet": Add a new pet to the store:\n',res.status_code, res.json(), sep='', end='\n\n')

res = requests.get(f"{base_url}/pet/{petId}", headers=headers)
print(f'Запрос GET/pet/petId": Find pet by ID:\n', res.status_code, res.text, sep='', end='\n\n')

files = {
'file': ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')
}
res = requests.post(f"{base_url}/pet/{petId}/uploadImage", headers={'accept':'application/json'}, files=files)
print(f'Запрос POST/pet/petId/uploadImage": uploadImage:\n', res.json(), sep='', end='\n\n')

data_pet_1_update = {
  "id": 1,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Chucha",
  "photoUrls": [
    "photoUrls"
  ],
  "tags": [
    {
      "id": 11,
      "name": "string"
    }
  ],
  "status": "sold"
}
res = requests.put(f"{base_url}/pet", headers=headers, json=data_pet_1_update)
print('Запрос PUT/: Updated an existing pet:', res.status_code, res.json(), sep='\n', end='\n\n')
#
# res = requests.get(f"{base_url}/pet/{petId}", headers=headers)
# print(f'Запрос GET/pet/petId": Find pet by ID:\n', res.status_code, res.text, sep='', end='\n\n')

res = requests.get(f"{base_url}/pet/findByStatus", headers=headers, params={'status': 'sold'})
print(f'Запрос GET/pet/findByStatus": Finds pets by status:\n', res.status_code, res.text, sep='', end='\n\n')

res = requests.get(f"{base_url}/pet/{petId}", headers=headers)
print(f'Запрос GET/pet/petId: Find pet by Id":\n', res.status_code, res.text, sep='', end='\n\n')

res = requests.post(f"{base_url}/pet/{petId}", headers={'accept': 'application/json'}, data={'name': 'Hichkok', 'status': 'pending'})
print(f'Запрос POST/pet/petId": Updates a pet in the store with form data:\n', res.json(), sep='', end='\n\n')

res = requests.delete(f"{base_url}/pet/{petId}/", headers=headers)
print(f'Запрос DEL/pet/petId: Deletes a pet:', res.text, sep='\n', end='\n\n')


### store: Access to Petstore orders ####
print('**************************   store   **********************************')
order = {
  "id": 1,
  "petId": 1,
  "quantity": 1,
  "shipDate": "2023-07-18T13:36:56.448Z",
  "status": "placed",
  "complete": True
}
orderId = 1

res = requests.post(f"{base_url}/store/order", headers={'accept': 'application/json'}, json=order)
print(f'Запрос POST/pet/Place an order for a petId": Place an order for a pet:\n', res.status_code, res.json(), sep='', end='\n\n')

res = requests.get(f"{base_url}/store/order/{orderId}", headers=headers)
print(f'Запрос GET/store/order/orderId: Find purchase order by Id":\n', res.status_code, res.text, sep='', end='\n\n')

res = requests.delete(f"{base_url}/store/order/{orderId}", headers=headers)
print(f'Запрос DELETE/store/order/orderId: Delete purchase order by Id":\n', res.status_code, res.text, sep='', end='\n\n')

res = requests.get(f"{base_url}/store/inventory", headers=headers)
print(f'Запрос GET/store/inventory: Returns pet inventories by status":\n', res.status_code, res.text, sep='', end='\n\n')
