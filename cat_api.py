import requests
import json
import webbrowser
import credentials
from pprint import pprint
import webbrowser


def add_favourite_cat(cat_id, user_id, headers):
    params = {
        "image_id": str(cat_id),
        "sub_id": user_id
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites', json=params, headers=headers)
    return r


def cat_user_interface(key, user_id, name):
    headers = {
        'x-api-key': credentials.auth_key
    }
    params = {
        'sub-id': user_id

    }

    try:
        print('Your favourite cats:')
        r = requests.get('https://api.thecatapi.com/v1/favourites/', params=params, headers=headers)
        pprint(r.json())
        favourite_cats = {cat['id']: cat['image']['url']
                          for cat in r.json()}
    except:
        print('error')
    else:
        response = input('Do you want to add a random cat to your favourites? Y/N\n*')
        if response.upper() == 'Y':
            try:
                r1 = requests.get('https://api.thecatapi.com/v1/images/search')
                print(r1.json())
                random_cat_url = r1.json()[0]['url']
                response1 = input('Do you want to add this cat? Y/N\n*')
                if response1.upper() == 'Y':
                    r4 = add_favourite_cat(r1.json()[0]['id'], user_id, headers)
                    print('Your favourite cats:')
                    favourite_cats.update({r4.json()['id']: random_cat_url})
                    print(favourite_cats)
                print('deleted')
                id_to_delete = input('pass id of the cat you would like to delete: ')
                r3 = requests.delete('https://api.thecatapi.com/v1/favourites/'+id_to_delete,
                                     headers=headers)
                print(r3.text)
                print('Your fave cats:')
                favourite_cats.pop(int(id_to_delete))
                print(favourite_cats)


            except:
                print('error')
    return


cat_user_interface(credentials.auth_key, 'my-user-1234', 'Wiktoria')
