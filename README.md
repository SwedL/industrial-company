<p align="center"><img src="https://i.ibb.co/xYsQMXR/Industrial-Company.png" alt="Industrial-Company" border="0" width="200"></p>

<p align="center">
   <img src="https://img.shields.io/badge/Pyhton-3.11-orange)" alt="Python Version">
   <img src="https://img.shields.io/badge/Django-5.0.3-E86F00" alt="Django Version">
</p>

<p>Приложение для сайта промышленной компании, выполненное по тестовому заданию. <br>
Штат сотрудников компании более 50000 человек</p>


## Описание работы приложения
Приложение состоит из четырёх интерфейсов. 

* Авторизация пользователя
* Древовидная структура компании
* Страница списка сотрудников, сгруппированных по выбранным параметрам поиска
* Интерфейс администратора для приёма и распределения сотрудников

### Авторизация пользователя
Страница, после авторизации, на которой, можно будет получить доступ к информации приложения, в зависимости от прав пользователя.

<a href="https://ibb.co/Ph7QmCY"><img src="https://i.ibb.co/d2dgWKc/2024-03-08-14-02-52.png" alt="2024-03-08-14-02-52" border="0"></a>

### Древовидная структура компании

<a href="https://ibb.co/nMPZBbq"><img src="https://i.ibb.co/HTh1CVL/2024-03-11-07-05-01.png" alt="2024-03-11-07-05-01" border="0"></a>

<table>
   <thead>
   <tr>
      <th scope="col" style="width:50%">Пользователь без прав изменения данных</th>
      <th scope="col" style="width:50%">Пользователь с правами изменения данных</th>
   </tr>
   </thead>
   <tbody>
      <tr>
         <td>
            может переходить по блокам отделов и должностей менеджеров
         </td>
         <td>
            дополнительно получает возможность снимать с должности и менять менеджеров используя <span style="font-weight: bold">drag-n-drop</span> сразу в дереве структуры компании
         </td>
      </tr>
      <tr>
         <td>
            <a href="https://ibb.co/fqFCRxQ"><img src="https://i.ibb.co/gm9D1R6/test-user-without-permission-1.gif" alt="test-user-without-permission-1" border="0" width="300"></a>
         </td>
         <td>
            <a href="https://ibb.co/9T4qgt2"><img src="https://i.ibb.co/9T4qgt2/image.gif" alt="image" border="0"></a>
         </td>
      </tr>
      <tr>
         <td>
         </td>
         <td>
            Изменение базы данных происходит путём обмена сообщений канала <span style="font-weight: bold">Websocket</span>
         </td>
      </tr>
   </tbody>
</table>

### Страница списка сотрудников
<a href="https://ibb.co/s5jpDFV"><img src="https://i.ibb.co/TKcDnHg/2024-03-11-07-06-50.png" alt="2024-03-11-07-06-50" border="0"></a>
<table>
   <thead>
   <tr>
      <th scope="col" style="width:50%">Пользователь без прав изменения данных</th>
      <th scope="col" style="width:50%">Пользователь с правами изменения данных</th>
   </tr>
   </thead>
   <tbody>
      <tr>
         <td>
            может искать сотрудников, подходящих под условия в фильтрах поиска
         </td>
         <td>
            дополнительно может изменять данные сотрудника компании, такие как должность и заработную плату
         </td>
      </tr>
      <tr>
         <td>
            <a href="https://ibb.co/znMLSJW"><img src="https://i.ibb.co/HFSMrdL/2024-03-10-14-37-51.gif" alt="2024-03-10-14-37-51" border="0" width="300"></a>
         </td>
         <td>
            <a href="https://ibb.co/hYsHQn8"><img src="https://i.ibb.co/9Zn2KfY/2024-03-10-14-59-47.gif" alt="2024-03-10-14-59-47" border="0" width="300"></a>
         </td>
      </tr>
      <tr>
         <td>
         </td>
         <td>
            Перевести сотрудника можно только на должность, у которой есть вакансии. <br>
            Изменение данных происходит без перезагрузки страницы с использованием запросов <span style="font-weight: bold">AJAX</span>
         </td>
      </tr>
   </tbody>
</table>

### Интерфейс администратора "приём и распределение сотрудников"
Страница доступная только пользователю с разрешением изменения данных. <br>
Здесь в компанию принимается новый сотрудник, далее он попадает в список снятых с должности или нераспределённых сотрудников, где можно назначить на должность или уволить

<a href="https://ibb.co/hFk6hyk"><img src="https://i.ibb.co/yFD9GXD/2024-03-11-07-08-00.png" alt="2024-03-11-07-08-00" border="0"></a>


## Установка

Скачайте код:
```sh
git clone https://github.com/SwedL/industrial-company.git
```
Перейдите в каталог проекта `industrial-company`, создайте виртуальное окружение, выполнив команду:

- Windows: `python -m venv venv`
- Linux: `python3 -m venv venv`

Активируйте его командой:

- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`


Создайте файл `.env` с переменными окружения и положите туда такой код:<br>

```sh
DEBUG=True
SECRET_KEY='vu1c-=svhigsn81!1doknfa2zxchlq&^37vdyqgc165a8wswjr'
ALLOWED_HOSTS='127.0.0.1 localhost'
INTERNAL_IPS='127.0.0.1 localhost'

POSTGRES_USER=user
POSTGRES_PASSWORD=user_pass
POSTGRES_DB=user_db

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=user_db
SQL_USER=user
SQL_PASSWORD=user_pass
SQL_HOST=localhost
SQL_PORT=5432
```
! **Важно**: SECRET_KEY замените на свой.<br>
Если вы хотите использовать базу данных `PostgreSQL`, то замените настройки доступа к базе данных на свои.

Если хотите использовать базу данных по умолчанию `SQLite`,
то файле `settings.py` каталога `ic` поменяйте базу данных на `SQLite`

Перейдите в каталог `project` и установите зависимости в виртуальное окружение:

```sh
pip install -r requirements.txt
```

Создайте необходимые таблицы базы данных командой:
```sh
python manage.py migrate
```

Для наполнения базы данных списком должностей, загрузите фикстуру командой:

- Windows: `python manage.py loaddata structure\fixtures\positions.json`
- Linux: `python manage.py loaddata structure/fixtures/positions.json`

Для наполнения базы фейковыми данными сотрудников можно воспользоваться скриптом, путь его размещения `structure/management/commands/init_employees.py`<br>
Команда запуска:
```sh
python manage.py init_employees
```
Возможно для наполнения базы сотрудниками потребуется какое-то время
<a href="https://ibb.co/N1HcPRr"><img src="https://i.ibb.co/RhVRm8N/init-employees1.png" alt="init-employees1" border="0"></a>
Создайте модель суперпользователя командой:
```sh
python manage.py createsuperuser
```

Запустите сервер:
```sh
python manage.py runserver
```
Для добавления разрешения на изменения данных новому пользователю необходимо выдать право **structure.change_employee**

## Как запустить версию сайта в docker.
Скачайте код:
```sh
git clone https://github.com/SwedL/industrial-company.git
```
Приложение в docker настроено на работу с использованием базы данных PostgreSQL.

Перейдите в каталог проекта `industrial-company`.<br>
Создайте файл `.env` с переменными окружения и положите туда такой код:<br>

```sh
DEBUG=True
SECRET_KEY='vu1c-=svhigsn81!1doknfa2zxchlq&^37vdyqgc165a8wswjr'
ALLOWED_HOSTS='127.0.0.1 localhost'
INTERNAL_IPS='127.0.0.1 localhost'

POSTGRES_USER=user
POSTGRES_PASSWORD=user_pass
POSTGRES_DB=user_db

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=user_db
SQL_USER=user
SQL_PASSWORD=user_pass
SQL_HOST=postgres
SQL_PORT=5432
```
**! Важно**: SECRET_KEY замените на свой.<br>

Затем выполните сборку и запуск образа:
```sh
docker-compose up -d
```
Если необходимо наполнить базу фейковыми данными сотрудников, используйте команду:
```sh
docker exec -it ic_project python manage.py init_employees
```
Создайте суперпользователя:
```sh
docker exec -it ic_project python manage.py createsuperuser
```


### Тестирование

Проект покрыт тестами моделей, форм, представлений и url.<br>
Тесты запускаются командой:
```sh
python manage.py test
```
В docker:
```sh
docker exec -it ic_project python manage.py test
```
## Автор проекта

* **Осминин Алексей** - [SwedL](https://github.com/SwedL)

