<p align="center"><img src="https://i.ibb.co/xYsQMXR/Industrial-Company.png" alt="Industrial-Company" border="0" width="200"></p>

<p align="center">
   <img src="https://img.shields.io/badge/Pyhton-3.12-orange)" alt="Python Version">
   <img src="https://img.shields.io/badge/Django-5.2-E86F00" alt="Django Version">
</p>

<p>Приложение для сайта промышленной компании, выполненное по тестовому заданию. <br>
Штат сотрудников компании более 50000 человек</p>

Рабочую версию сайта вы можете посмотреть на [https://icompany-pro.ru](https://icompany-pro.ru)

## Описание работы приложения
Приложение состоит из четырёх интерфейсов. 

* Авторизация пользователя
* Древовидная структура компании
* Страница списка сотрудников, сгруппированных по выбранным параметрам поиска
* Интерфейс администратора для приёма и распределения сотрудников

### Авторизация пользователя
Страница, после авторизации, на которой, можно будет получить доступ к информации приложения, в зависимости от прав пользователя.

<a href="https://i.ibb.co/d2dgWKc/2024-03-08-14-02-52.png"><img src="https://i.ibb.co/d2dgWKc/2024-03-08-14-02-52.png" alt="image" border="0"></a>

### Древовидная структура компании

<a href="https://i.ibb.co/HTh1CVL/2024-03-11-07-05-01.png"><img src="https://i.ibb.co/HTh1CVL/2024-03-11-07-05-01.png" alt="image" border="0"></a>

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
            <a href="https://i.ibb.co/gm9D1R6/test-user-without-permission-1.gif"><img src="https://i.ibb.co/gm9D1R6/test-user-without-permission-1.gif" alt="gif" border="0" width="300"></a>
         </td>
         <td>
            <a href="https://i.ibb.co/J29CXm6/test-user-with-permission.gif"><img src="https://i.ibb.co/J29CXm6/test-user-with-permission.gif" alt="gif" border="0" width="300"></a>            
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
- переход в подразделение компании, осуществляется при нажатии на подразделение в древовидной структуре компании  

<a href="https://i.ibb.co/TKcDnHg/2024-03-11-07-06-50.png"><img src="https://i.ibb.co/TKcDnHg/2024-03-11-07-06-50.png" alt="image" border="0"></a>
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
            <a href="https://i.ibb.co/HFSMrdL/2024-03-10-14-37-51.gif"><img src="https://i.ibb.co/HFSMrdL/2024-03-10-14-37-51.gif" alt="gif" border="0" width="300"></a>
         </td>
         <td>
            <a href="https://i.ibb.co/9Zn2KfY/2024-03-10-14-59-47.gif"><img src="https://i.ibb.co/9Zn2KfY/2024-03-10-14-59-47.gif" alt="gif" border="0" width="300"></a>
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

<a href="https://i.ibb.co/yFD9GXD/2024-03-11-07-08-00.png"><img src="https://i.ibb.co/yFD9GXD/2024-03-11-07-08-00.png" alt="image" border="0"></a>


## Запуск сервера:

### Локально в Docker контейнере 

- Склонируйте репозиторий:
```
git clone https://github.com/SwedL/industrial-company.git
```
 - Перейдите в каталог проекта
```
cd industrial-company
```
- Установите переменные окружения. Создайте файл .env и скопируйте содержимое из .env.dev.example, подставьте свои значения.
- Запустите контейнеры.
```
docker compose up --build
```
Создайте модель суперпользователя
- Войдите в терминал контейнера с помощью команды:
```
docker exec -it project bash
```
- Создайте суперпользователя:
```
python3 manage.py createsuperuser
```
- Для наполнения базы фейковыми данными сотрудников можно воспользоваться скриптом<br>
Команда запуска:
```
python3 manage.py init_employees
```

### На удалённом сервере в Docker контейнере 

- Склонируйте репозиторий:
```
git clone https://github.com/SwedL/industrial-company.git
```
 - Перейдите в каталог проекта
```
cd industrial-company
```
- Установите переменные окружения. Создайте файл .env и скопируйте содержимое из .env.prod.example, подставьте свои значения.
- Создайте директории для certbot, выполнив:
```
mkdir -p certbot/conf
mkdir certbot/www
```
- Измените в docker-compose.prod.yml в строке 75 ваш <ins>email</ins> и <ins>ваш домен</ins>, для получения SSL-сертификата от Let's Encrypt
- Перейдите в директорию nginx/prod/default.conf и в строках 4, 17, 19, 20 установите значение <ins>вашего домена</ins>
- Запустите контейнеры.
```
docker compose -f docker-compose.prod.yml up --build
```
Создайте модель суперпользователя
- Войдите в терминал контейнера с помощью команды:
```
docker exec -it project bash
```
- Создайте суперпользователя:
```
python3 manage.py createsuperuser
```
- Для наполнения базы фейковыми данными сотрудников можно воспользоваться скриптом<br>
Команда запуска:
```
python3 manage.py init_employees
```

## Структура проекта

```
industrial-company/
├── nginx/               # Директория конфигурационных файлов обратного прокси сервера           
│   └── ...   
└── project/             # Директория Django проекта
    ├── ic/              # Django проект ic
    │   └── ... 
    ├── structure/       # Приложение structure
    │   ├── consumers/   # Обработка асинхронных событий websocket соединений
    │   ├── fixtures/    # Начальные данные для заполнения БД
    │   ├── management/  # Собственные скрипты проекта для manage.py
    │   ├── migrations/   
    │   ├── permissions/ # Функции-разрешения для пользователей
    │   ├── services/    # Сервисы - выполняют операции над данными
    │   ├── static/       
    │   ├── templates/    
    │   ├── tests/       # Тесты шаблонов, форм, представлений
    │   ├── admin.py     
    │   ├── models.py    
    │   ├── routing.py   # Маршрутизация асинхронных событий websocket соединений
    │   ├── urls.py      
    │   ├── views.py     
    │   └── ...
    ├── Dockerfile    
    ├── manage.py    
    └── pyproject.toml   # Конфигурация Poetry    
```

### Тестирование

Проект покрыт тестами моделей, форм, представлений и url.<br>
Тесты запускаются командой:
```
python manage.py test
```
В docker:
```
docker exec -it project python manage.py test
```
## Автор проекта

* **Осминин Алексей** - [SwedL](https://github.com/SwedL)
