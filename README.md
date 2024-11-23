# Django Blog API

Проект предоставляет API для блога с функциональностью регистрации пользователей, создания постов и комментариев. Этот проект использует Django, Django REST Framework и библиотеку для авторизации через JWT.

## Шаги для установки и запуска проекта на другом компьютере

### 1. Клонирование репозитория:

Сначала клонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/keyayeten/test_api.git
cd yourproject
```
### 2. Создание виртуального окружения:
Рекомендуется использовать виртуальное окружение для изоляции зависимостей проекта. Для этого выполните следующие шаги:

Для Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
Для macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей:

Установите все необходимые зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Этот файл включает все нужные библиотеки для работы проекта, такие как:

- Django
- Django REST Framework
- Djoser (для JWT аутентификации)
- Faker (для наполнения базы данных фейковыми данными)

### 4. Настройка базы данных:
Выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создание суперпользователя:
Для создания суперпользователя, с помощью которого вы сможете войти в админку Django, выполните команду:
```bash
python manage.py createsuperuser
```

### 6. Наполнение базы данных фейковыми данными:
```bash
python manage.py fill_db
```

### 7. Сбор статики
Для правильной работы статики в Django необходимо собрать файлы статики. Выполните команду:
```bash
python manage.py collectstatic
```
Это скопирует все статические файлы (CSS, JavaScript, изображения и т.д.) в директорию, указанную в настройках STATIC_ROOT.

### 8. Запуск сервера
```bash
python manage.py runserver
```

### 8. Запуск сервера
Откройте http://127.0.0.1:8000/swagger/ для просмотра документации API.
