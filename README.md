# jobhunter
Публикует статистику уровня заработной платы в Москве по вакансиям для программистов на
https://hh.ru и https://spb.superjob.ru/

## Цель проекта
Учебный проект на https://dvmn.org/t/middle-python-dev-before-you-finish-the-course/

## Как установить
Для установки зависимостей воспользуйтесь командой 'pip' или 'pip3'.

```
  pip install -r requirements.txt
```

Получите токен [SuperJob](https://api.superjob.ru/) сохраните его в файле .env 

```
SUPERJOB_TOKEN=<YOUR_SUPERJOB_TOKEN>
```

## Как использовать

#### Статистика за последние 30 дней
``` 
  python3 jobhunter.py
```

#### Статистика начиная с желаемой даты. Формат даты 'гггг-мм-дд'
``` 
  python3 jobhunter.py '2022-08-25'
```
