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

<a href="https://ibb.co/vhSWD9r"><img src="https://i.ibb.co/bFkV7ty/2024-03-10-19-01-52.png" alt="2024-03-10-19-01-52" border="0"></a>

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
            <a href="https://ibb.co/9T4qgt2"><img src="https://i.ibb.co/J7pztQ2/image.gif" alt="image" border="0" width="300"></a>
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
<a href="https://ibb.co/Sm2sKTC"><img src="https://i.ibb.co/T0ZvHX3/2024-03-10-19-00-03.png" alt="2024-03-10-19-00-03" border="0"></a>
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

### Интерфейс администратора <наём и распределение сотрудников>
Страница доступная только пользователю с разрешением изменения данных. <br>
Здесь в компанию принимается новый сотрудник, далее он попадает в список снятых с должности или нераспределённых сотрудников, где можно назначить на должность или уволить


<a href="https://ibb.co/mSLCRCX"><img src="https://i.ibb.co/7bwJSJR/2024-03-10-18-57-25.png" alt="2024-03-10-18-57-25" border="0"></a>



## Установка

Предварительно создайте директорию для приложения (some directory)<br>
Клонируйте код репозитория в созданную директорию (в some directory):
```sh
git clone https://github.com/SwedL/industrial-company.git
```
Также в каталоге проекта (some directory) создайте виртуальное окружение, выполнив команду:

- Windows: `python -m venv venv`
- Linux: `python3 -m venv venv`

Активируйте его командой:

- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`


Перейдите в каталог industrial-company и установите зависимости в виртуальное окружение:
```sh
cd industrial-company
```
```sh
pip install -r requirements.txt
```

Создайте файл `.env` в каталоге
`industrial-company/` и положите туда такой код:

! **Важно**: SECRET_KEY замените на свой
```sh
DEBUG=True
SECRET_KEY='vu1c-=svhigsn81!1doknfa2zxchlq&^37vdyqgc165a8wswjr'
```

Создайте файл базы данных SQLite и проведите миграции моделей командами:
```sh
python manage.py makemigrations
python manage.py migrate
```

Для наполнения базы данных списком должностей, загрузите фикстуру командой:

- Windows: `python manage.py loaddata structure\fixtures\positions.json`
- Linux: `python manage.py loaddata structure/fixtures/positions.json`

Для наполнения базы фейковыми данными сотрудников можно воспользоваться скриптом, путь его размещения structure/management/commands/init_employees.py<br>
Команда запуска:
```sh
python manage.py init_employees
```

Создайте модель суперпользователя командой:
```sh
python manage.py createsuperuser
```

Запустите сервер:
```sh
python manage.py runserver
```
Для добавления разрешения на изменения данных новому пользователю необходимо выдать право **structure.change_employee**

### Тестирование

Проект покрыт различными тестами, которые проверяют его работоспособность.<br>
Тесты запускаются командой:
```sh
python manage.py test
```
## Автор проекта

* **Осминин Алексей** - [SwedL](https://github.com/SwedL)

