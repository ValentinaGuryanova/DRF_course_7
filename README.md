# DRF_course_7 (Трекер полезных привычек)

## Для работы с проектом необходимо выполнить следующие действия:

- Клонировать репозиторий.
- Активировать виртуальное окружение venv/bin/activate.bat
- Установить зависимости pip install -r requirements.txt
- Создать файл .env, заполнить его данными из файла env.sample
- Установить и запустить Redis
- Создать базу данных в PostreSQL CREATE DATABASE drf_course_7
- Создать python manage.py makemigrate и применить миграции python manage.py migrate
- Запустить проект python manage.py runserver
- Запустить  celery -A config worker -l info -P eventlet, celery -A config Beat -l info -S django
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.

## Решены следующие задачи:

- Настроено CORS
- Настроена интеграция с Telegram
- Реализована пагинация
- Использованы переменные окружения
- Все необходимые модели описаны или переопределены
- Все необходимые эндпоинты реализовали
- Настроены все необходимые валидаторы
- Описанные права доступа заложены
- Настроена отложенная задача через Celery
- Проект покрыт тестами как минимум на 80%
- Код оформлен в соответствии с лучшими практиками
- Имеется список зависимостей
- Результат проверки Flake8 равен 100%, при исключении миграций
- Решение выложено на GitHub

## Описание задач

- Добавлены необходимые модели привычек
- Реализованы эндпоинты для работы с фронтендом
- Создано приложение для работы с Telegram и рассылками напоминаний

## Модель Привычка:

- Пользователь — создатель привычки.
- Место — место, в котором необходимо выполнять привычку.
- Время — время, когда необходимо выполнять привычку.
- Действие — действие, которое представляет из себя привычка.
- Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
- Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
- Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
- Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
- Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

## Модель Пользователь:

- почта,
- телефон,
- город,
- аватар.
  
## Валидаторы

- Исключить одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

## Пагинация

Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

## Права доступа

- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

## Эндпоинты

- Регистрация
- Авторизация
- Список привычек текущего пользователя с пагинацией
- Список публичных привычек
- Создание привычки
- Редактирование привычки
- Удаление привычки

## Интеграция

Для полноценной работы сервиса необходим реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.
Для этого потребуется интегрировать сервис с мессенджером Telegram, который будет заниматься рассылкой уведомлений.

## Безопасность

Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

## Документация

Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. При необходимости эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную.

Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:

http://127.0.0.1:8000/docs/
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/

## Тестирование проекта

Для тестирования проекта запустить команду: python3 manage.py test
