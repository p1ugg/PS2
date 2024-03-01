# Программа для создания резюме

## Как проходит процесс

Программа делает запрос к API сервера МИЭМа, GitHub, GitLab

# _Как запустить файл у себя_

## Подключение переменных среды:

```
В tk.py измените значение MIEM_TOKEN наличный токен аутентификации 
для личного кабинета МИЭМ cabinet.miem.hse.ru

GITHUB_USERNAME = имя пользователя в GitHub
GITHUB_TOKEN = персональный токен для GitHub API

GITLAB_TOKEN = Ваш токен от Gitlab
GITLAB_REPO_URL = id репозитория в GitLab
```

### Получения токена от личного кабинета МИЭМ

1. Зайти в [личный кабинет](https://cabinet.miem.hse.ru/profile#/student-profile)
2. Открыть в консоли вкладку Network
3. Перезагрузить страницу
4. Посмотреть в запросе "student_profile" заголовок "X-Auth-Token"

### Получение токена от Git Hub
[Документация от Git Hub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)

### Получение токена от Git Lab
[Документация Git Lab API](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

## Виртуальное окружение(опционально)

### Создание:

```python 
python -m venv venv
```

### Активация на Windows:

```python 
venv/scripts/activate
```

### Активация на Unix-like:

```python 
venv/bin/activate
```

## Подключение необходимых библиотек.

```python
pip install -r requirements.txt
```

## Запуск программы.

```python
python main.py
```