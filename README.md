# Аналитика данных о торговых точках
## Условие
Клиенту был отправлен запрос на данные для более детального изучения ситуации на  
торговых точках на Урале и в Сибири необходимы понедельные продажи  
в этих точках за период с 1 января 2018 года, а так же описание точек: город,  
координаты, дата открытия, дата закрытия.  
В ответ клиент прислал письмо с файлом  
`Copy of Copy of Export Store_Sales Jan'18 Nov'19 final.xlsx`  

## Задача
Необходимо организовать данные в две таблицы stores и sales , затем  
проанализировать полученный набор данных на предмет ошибок /  
неоднозначностей / несоответствий в данных. Особое внимание необходимо  
уделить проверке соответствия данных исходному запросу.  

## Резюитруя
Что ожидаем получить на выходе:  
- датасет из двух текстовых таблиц stores и sales и код, который собирает
- его из исходного файла
- перечень найденных проблем в данных и код для анализа датасета


## Навигация:
`conf.py` - пути к исходному сету и итоговому
`main.py` - скрипт по сборе датасета
`store.py`, `sales.py` - функции возвращающие соответствующие фреймы
`errors.txt` - найденные ошибки
`dataset.xlsx` - итоговый датасета
`analyze.ipynb` - анализ готового датасета с комметариями к аналитикам
`requirements.txt` - зависимости проекта
