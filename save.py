from threading import Thread
import requests
from data.config import ADDRES

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def save_user(message, number=None, address=None) -> int():
    post_data = {
        'tg_id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'number': number,
        'address': address,
    }
    x = requests.post(url=f'{ADDRES}user/register/', data=post_data)
    return x.status_code


@threaded
def save_korzina(message, product, price, count):
    post_data = {
        'user_id': message.from_user.id,
        'product': product,
        'price': price,
        'count': count,
    }
    requests.post(url=f'{ADDRES}korzina/create/', data=post_data)


@threaded
def del_korzina(pk):
    requests.delete(url=f'{ADDRES}korzina/delete/{pk}')


def Create_order(product, price, address, number, user):
    data = {
        "product": f"{product}",
        "price": f"{price}",
        "address": f"{address}",
        "number": f"{number}",
        "order": 'Kutilmoqda',
        "user": user
    }
    x = requests.post(url=f'{ADDRES}order/', data=data)
    return [x.status_code, x.text]


def OrderConfirm(pk):
    data = {
        "order": 'Tasdiqlandi',
    }
    requests.patch(url=f'{ADDRES}order/update/{pk}/', data=data)


def OrderCalcel(pk):
    data = {
        "order": 'Bekor Qilindi',
    }
    requests.patch(url=f'{ADDRES}order/update/{pk}/', data=data)


def OrderKuryer(pk, kuryer):
    data = {
        "kuryer": kuryer,
    }
    requests.patch(url=f'{ADDRES}order/update/{pk}/', data=data)


def OrderKuryerClear(pk):
    data = {
        "kuryer": "",
    }
    requests.patch(url=f'{ADDRES}order/update/{pk}/', data=data)


def Orderdate(pk, date):
    data = {
        "date": date,
    }
    requests.patch(url=f'{ADDRES}order/update/{pk}/', data=data)


def OrderCleardate(pk):
    data = {
        "date": "",
    }
    requests.patch(url=f'{ADDRES}order/update/{pk}/', data=data)
