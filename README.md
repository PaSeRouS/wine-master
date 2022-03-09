# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Запустите сайт командой 
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Также при запуске можно указать параметр --filename, после которого указывается путь к файлу с напитками (по умолчанию - "products.xlsx").

В файле данные хранятся в следующем виде:

Категория    | Название      | Сорт            | Цена | Картинка          | Акция                |
-------------|---------------|-----------------|------|-------------------|----------------------|
Белые вины   | Белая леди    | Дамский пальчик | 399  | belaya_ledi.png   | Выгодное предложение |
Красные вины | Черный лекарь | Качич           | 399  | chernyi_lekar.png |                      |
Напитки      | Чача          |                 | 299  | chacha.png        | Выгодное предложение |

Изображения из стоблца "Картинка" должны лежать в папке images.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
