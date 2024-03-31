import requests
import os

def get_address_from_coords(coords):
    PARAMS = {
        "apikey": os.environ.get('apikey'),
        "format": "json",
        "lang": "uz",
        "kind": "house",
        "geocode": coords
    }
    try:
        r = requests.get(url="https://geocode-maps.yandex.ru/1.x/", params=PARAMS)
        json_data = r.json()
        address_str = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
        return address_str
    except Exception as e:
        return "Map aniqlay olmadi😔, tashvishlanmang xodimlar locatsiyadan aniqlaydi."

