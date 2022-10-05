import re
import vk_api
from configures import token_vk, bot_token
from VKUser import VKUser
from datetime import date


def get_user_info(user_id):
    vk = vk_api.VkApi(token=bot_token)
    response = vk.method('users.get', {'user_ids': user_id, 'fields': 'bdate, sex, city, relation'})
    result = response[0]

    bdate_pattern = r'\d{1,2}.\d{1,2}.\d{4}'

    if 'city' in result:
        city = result['city']['title']
    else:
        city = 'Город не указан'

    if 'bdate' in result and re.match(bdate_pattern, result['bdate']):
        bdate = result['bdate']
    else:
        bdate = date.today()

    info = VKUser(result['id'], result['first_name'], result['last_name'], bdate,
                  result['sex'], city)

    info.url = f"https://vk.com/id{result['id']}"

    return info


#отправляет запросы к ВК, количество предложенных запросов в параметре count
def search_possible_pair(sex, age_from, age_to, city, count):
    possible_list = []
    vk = vk_api.VkApi(token=token_vk)
    response = vk.method('users.search', {'sex': sex, 'status': 6, 'age_from': age_from,
                                          'age_to': age_to, 'has_photo': 1,
                                          'count': count, 'online': 0, 'hometown': city})

    for item in response['items']:
        vk_user = get_user_info(item['id'])
        possible_list.append(vk_user)

    return possible_list


def get_photos(person_id):
    vk = vk_api.VkApi(token=token_vk)
    try:
        response = vk.method('photos.get', {'owner_id': person_id, 'album_id': 'profile',
                                            'extended': 1,
                                            'photo_sizes': 1})
    except vk_api.exceptions.ApiError:
        print('Closed profile')
        return {}

    print(response)

    users_photos = []
    user_photos_dict = {}

    for item in response['items']:
        users_photos.append([response['items'][item]['likes']['count'],
                             response['items'][item]['id']])

    photos = sorted(users_photos, key=lambda x: int(x[0]), reverse=True)
    photos_three = photos[:3] if len(photos) >= 3 else photos
    print(photos_three)
    for photo in photos_three:
        user_photos_dict[photo[1]] = photo[0]

    return user_photos_dict
