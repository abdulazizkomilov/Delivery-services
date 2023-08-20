import requests


def get_address_from_coords(coords):
    PARAMS = {
        "apikey": "5be3c86c-b9d7-4451-ad06-f60e4f6276b7",
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

# if __name__ == '__main__':
#     # даем запрос на получение адреса с координатами 37.617585, 55.751903
#     address_str = get_address_from_coords("69.541947, 41.454158,")
#     # распечатываем адрес
#     print(address_str)
