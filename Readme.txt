1) Переход по директориям:
127.0.0.1:port/templates
2)Создание пустой дирректории
127.0.0.1:port/create/?q=123
для дальнейшей работы со строкой нужно привести урл к виду 
127.0.0.1:port/
т.е. стереть все до create включая create
3)Удалеие дирректории
127.0.0.1:port/delete/?q=123
для дальнейшей работы со строкой нужно привести урл к виду 
127.0.0.1:port/
т.е. стереть все до delete включая delete
4)загрузка файлов с сервера на компьютер
127.0.0.1:port/downlo/?q=apps.py
для дальнейшей работы со строкой нужно привести урл к виду 
127.0.0.1:port/
5)загрузка файлов с компьютера на сервер
127.0.0.1:port/upload
дальше появится интерфейс
для дальнейшей работы со строкой нужно привести урл к виду 
127.0.0.1:port/
загрузка происходит в папку медиа, которая находится в корне

Описание протокола webdav
Hабор расширений и дополнений к протоколу HTTP, поддерживающих совместную работу пользователей над редактированием файлов и управление файлами на удаленных веб-серверах.

для проверки использовался
Mozilla Firefox 70.0.1

тестировать нужно в Debug mode, так как он сам выводит все exceptions(в настройках он уже стоит)

