# Windows
Устанавливаем Microsoft Visual C++\
https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/

Выполняем в PowerShell с правами администратора
```bash
Set-ExecutionPolicy RemoteSigned
```

Создаем виртуальное пространство и устанавливаем зависимости
```bash
python -m venv .\app\.venv
.\app\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\app\requirements.txt
```

Произведем миграцию моделей и запуск сервера
```bash
python .\app\manage.py migrate
python .\app\manage.py create_superuser --env=dev
python .\app\manage.py runserver
```

Для создания актуального списка зависимостей выполним
```bash
pip freeze > .\app\requirements.txt
```

Задаем параметры .env.dev и .env.prod

Создаем и запускаем контейнер
```bash
./docker-build.sh --env dev
```
или
```bash
./docker-build.sh --env prod
```

Для вывода логов докера используем
```bash
docker compose logs -f
```

# TO_DO
## Ожидание инициализации
Следует разобраться как исправить ситуацию, когда самая первая инициализация требует перезапуска (pg_isready возвращает флаг раньше, чем появляется реальный доступ к СУБД из приложения Django, поэтому migrations не выполняется).

### Вариант 1 (не нравится, хотелось бы решить через service_healthy):

Можно создать ./app/entrypoint.prod.sh, который будет вызываться из Dockerfile.prod

```bash
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
```

```bash
#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done

exec "$@"
```

### Вариант 2 (использование команды manage.py)

Добавление в **start.sh** проверки доступности БД решает вопрос, но при первом запуске кода был ложноположительный результат на который стоит обратить внимание 

```bash
python manage.py db_health_check
```

# Запуск

```
http://127.0.0.1:8000
```
