import requests
import json

url = "https://ws-api.toasttab.com/consumer-app-bff/v1/graphql"

payload = json.dumps([
  {
    "operationName": "MENUS",
    "variables": {
      "input": {
        "shortUrl": "cafe-square-one",
        "restaurantGuid": "f45640aa-3350-4e46-81a4-1712171ad916",
        "menuApi": "DO"
      }
    },
    "query": "query MENUS($input: MenusInput!) {\n  menusV3(input: $input) {\n    ... on MenusResponse {\n      menus {\n        id\n        name\n        groups {\n          guid\n          name\n          description\n          items {\n            description\n            guid\n            name\n            outOfStock\n            price\n            imageUrl\n            calories\n            itemGroupGuid\n            unitOfMeasure\n            usesFractionalQuantity\n            masterId\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    ... on GeneralError {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
  },
  {
    "operationName": "POPULAR_ITEMS",
    "variables": {
      "input": {
        "restaurantGuid": "f45640aa-3350-4e46-81a4-1712171ad916",
        "menusInput": {
          "restaurantGuid": "f45640aa-3350-4e46-81a4-1712171ad916",
          "shortUrl": "cafe-square-one",
          "menuApi": "DO"
        }
      }
    },
    "query": "query POPULAR_ITEMS($input: PopularItemsInput!) {\n  popularItems(input: $input) {\n    ... on PopularItemsResponse {\n      items {\n        name\n        guid\n        itemGroupGuid\n        imageUrl\n        price\n        __typename\n      }\n      __typename\n    }\n    ... on PopularItemsError {\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
  }
])
headers = {
  'Content-Type': 'application/json',
  'Cookie': '__cf_bm=T7Hb243xOCL8Kyl5UwBChaDFeZ.qnxZt.0.Wu5OVy5Q-1681487993-0-AX+u8H4IyVY2xhlchKXWXUIawhtsLBUJNETk0yOJjFDZJJbYPx9O+pX7hxoFI1vEDUcEZaPfJXf6Sm1FemqgtVo='
}

response = requests.request("POST", url, headers=headers, data=payload)

menus = response.json()[0].get('data').get('menusV3').get('menus')
food = menus[0].get('groups')
beverage = menus[1].get('groups')

# write to file
with open('food.csv', 'w') as f:
    #write line by line
    f.write('item_name;item_description;item_price;item_category')
    for fo in food:
        for i in fo.get('items'):
            category = fo.get('name')
            name = i.get('name')
            description = i.get('description')
            price = i.get('price')
            imageUrl = i.get('imageUrl')
            f.write(f'\n{name};{description};{price};{category}')

with open('beverage.csv', 'w') as f:
    #write line by line
    f.write('item_name;item_description;item_price;item_category')
    for fo in beverage:
        for i in fo.get('items'):
            category = fo.get('name')
            name = i.get('name')
            description = i.get('description')
            price = i.get('price')
            imageUrl = i.get('imageUrl')
            f.write(f'\n{name};{description};{price};{category}')
