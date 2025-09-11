# Python асинхронная библиотека для отправки SMS сообщений через SMS Aero API

[![PyPI version](https://badge.fury.io/py/smsaero-api-async.svg)](https://badge.fury.io/py/smsaero-api-async)
[![Python Versions](https://img.shields.io/pypi/pyversions/smsaero-api-async.svg)](https://pypi.org/project/smsaero-api-async/)
[![Downloads](https://pepy.tech/badge/smsaero-api-async)](https://pepy.tech/project/smsaero-api-async)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](MIT-LICENSE)

## Установка (из PyPI):

```bash
pip install -U smsaero-api-async
```

## Пример использования:

API-ключ вы можете получить в настройках аккаунта: https://smsaero.ru/cabinet/settings/apikey/

```python
import pprint
import asyncio
import smsaero


SMSAERO_EMAIL = 'ваш email'
SMSAERO_API_KEY = 'ваш api ключ'


async def send_sms(phone: int, message: str) -> None:
    """
    Отправляет SMS сообщение

    Параметры:
    phone (int): Номер телефона, на который будет отправлено SMS сообщение.
    message (str): Содержимое SMS сообщения для отправки.
    """
    api = smsaero.SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)
    try:
        result = await api.send_sms(phone, message)
        pprint.pprint(result)
    finally:
        await api.close_session()


async def send_telegram_code(phone: int, code: int) -> None:
    """
    Отправляет код Telegram

    Параметры:
    phone (int): Номер телефона, на который будет отправлен код Telegram.
    code (int): Код Telegram (от 4 до 8 цифр).
    """
    api = smsaero.SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)
    try:
        result = await api.send_telegram(phone, code)
        pprint.pprint(result)
    finally:
        await api.close_session()


if __name__ == '__main__':
    asyncio.run(send_sms(70000000000, 'Привет, Мир!'))
    asyncio.run(send_telegram_code(70000000000, 1234))
```

#### Исключения:

* `SmsAeroException` - базовый класс исключений для всех исключений, вызываемых библиотекой.
* `SmsAeroConnectionException` - исключение, вызываемое при ошибке соединения.
* `SmsAeroNoMoneyException` - исключение, вызываемое при недостатке средств на счете.


## Использование из командной строки:

```bash
SMSAERO_EMAIL="ваш email"
SMSAERO_API_KEY="ваш api ключ"

smsaero_send --email "$SMSAERO_EMAIL" --api_key "$SMSAERO_API_KEY" --phone 70000000000 --message 'Привет, Мир!'
```

## Запуск в Docker (demo):

```bash
docker pull 'smsaero/smsaero_python_async:latest'
docker run -it --rm 'smsaero/smsaero_python_async:latest' smsaero_send --email "ваш email" --api_key "ваш api ключ" --phone 70000000000 --message 'Привет, Мир!'
```

## Совместимость с версиями Python:

* Текущая версия библиотеки совместима с Python 3.7+.


## Лицензия:

```
MIT License
```
