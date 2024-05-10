# Trade Marketing Statistics Microservice

Этот проект представляет собой реализацию [тестового задания для стажёра Backend в команду Trade Marketing](https://github.com/Dark04072006/StatisticsMicroservice/assets/ТЗ.md). Он представляет собой микросервис для работы со статистическими данными.

## Технологический стек:

- **Язык программирования:** Python
- **База данных:** PostgreSQL
- **Контейнеризация:** Docker
- **Веб-фреймворк:** FastAPI
- **Драйвер для PostgreSQL:** Psycopg
- **Фреймворк для внедрения зависимостей:** Dishka

## Используемая архитектура:

Данный микросервис реализован с использованием принципов чистой архитектуры, также известной как архитектура Боба Мартина. Это обеспечивает высокую гибкость, масштабируемость и тестируемость приложения.

## Запуск с Docker
``` shell
docker-compose up
```

## Инструкция по установке

### 1. Клонирование репозитория
``` shell
git clone https://github.com/Dark04072006/StatisticsMicroservice
```

### 2. Переход в директорию проекта
``` shell
cd StatisticsMicroservice/
```

### 3. Установка зависимостей
``` shell
pip install -e .
```

#### также можно установить доп. пакеты для линтеров и тестирования:

``` shell
pip install -e .[lint,testing]
```

### 4. Создать скрипт env/env.sh, в котором будут переменные окружения. Заполнить следуя этому шаблону:

``` shell
#! /bin/bash

export POSTGRES_USER=required
export POSTGRES_PASSWORD=required
export POSTGRES_DB=required
export POSTGRES_HOST=required
export POSTGRES_PORT=required
export PYTHONPATH=StatisticsMicroservice
```

### 5. Предоставить доступ к скрипту запуска
``` shell
chmod +x scripts/start.sh
```

### 6. Запустить проект
``` shell
scripts/start.sh
```

## Документация REST API

#### GET /statistics/

Получение статистики в определенный период

**Параметры запроса:**

- `from` - дата начала периода (включительно)
- `to` - дата окончания периода (включительно)
- `sort_by` - (Опционально) Список полей, по которым будет отсортирована статистика. Доступные поля: ["date", "views", "clicks", "cost"]

**Пример запроса:**

``` http
GET /statistics/?from=2022-01-01&to=2022-12-31&sort_by=date
```

**Пример ответа:**

``` json
[
  {
    "date": "2022-01-01",
    "views": 1000,
    "clicks": 50,
    "cost": 500.00,
    "cpc": 10.00,
    "cpm": 500.00
  },
  {
    "date": "2022-01-02",
    "views": 1500,
    "clicks": 75,
    "cost": 600.00,
    "cpc": 8.00,
    "cpm": 400.00
  },
  ...
]
```

#### POST /statistics/

Сохранение статистики

**Тело запроса:**

``` json
{
  "date": "2022-01-01",
  "views": 1000,
  "clicks": 50,
  "cost": 500.00
}
```

**Пример запроса:**

``` http
POST /statistics/
Content-Type: application/json

{
  "date": "2022-01-01",
  "views": 1000,
  "clicks": 50,
  "cost": 500.00
}
```

**Пример ответа:**

``` json
{
  "date": "2022-01-01",
  "views": 1000,
  "clicks": 50,
  "cost": 500.00,
  "cpc": 10.00,
  "cpm": 500.00
}
```

#### DELETE /statistics/

Сброс всей сохраненной статистики

**Пример запроса:**

``` http
DELETE /statistics/
```

**Пример ответа:**

``` http
HTTP/1.1 204 No Content
```

## Лицензия

Смотрите файл [LICENSE](https://github.com/Dark04072006/StatisticsMicroservice/blob/main/LICENSE.md) для прав и ограничений лицензии (MIT).

## Проблемы

Если у вас возникли проблемы с проектом или у вас есть предложения по улучшению, пожалуйста, не стесняйтесь сообщить о них, [создав issue](https://github.com/Dark04072006/StatisticsMicroservice/issues) в репозитории GitHub. Мы рады вашим отзывам!

## Pull Requests

Если вы хотите внести свой вклад в этот проект, следуйте этим шагам:

1. Форкните репозиторий.
2. Создайте новую ветку для вашей функции или исправления ошибки.
3. Внесите изменения и убедитесь, что они правильно протестированы.
4. Предложите pull request (PR) в ветку `dev` оригинального репозитория.
5. Предоставьте подробное описание ваших изменений в описании PR.

## Контакт

- **Автор:** Алим Абреков
- **Email:** Abrekovalim38702@gmail.com
- **GitHub:** [https://github.com/Dark04072006](https://github.com/Dark04072006)
- **Telegram:** [https://t.me/some_usernamexD](https://t.me/some_usernamexD)
