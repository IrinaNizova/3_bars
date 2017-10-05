# Ближайшие бары
Программа выводит самый большой бар и самый маленький бар,
затем запрашивает данные о координатах пользователя и выводит самый близкий к нему бар.

Данные о барах можно получить так:

Зарегистрироваться на сайте data.mos.ru и получить ключ API;
скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.
А можно скачать файл с данными по ссылке
https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py [путь до файла с данными] ```
# Пример ответа


Самый большой бар Спорт бар «Красная машина» включает 450 посадочных мест
Самый маленький бар БАР. СОКИ включает 0 посадочных мест
Вы можете ввести свои координаты чтобы найти ближайший бар
Введине долготу: 37.3
Введите широту: 55.8
Ближайший бар это БАР. СОКИ
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
