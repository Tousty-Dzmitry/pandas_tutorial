# Работа с Pandas в Python

Этот проект демонстрирует основные операции с библиотекой Pandas в Python. Включает создание, чтение, индексирование, фильтрацию, обработку отсутствующих данных, агрегацию, группировку и изменение формы данных.

## Установка

Перед использованием убедитесь, что у вас установлен Pandas:

```bash
pip install pandas
```

## Основные возможности

### 1. Создание DataFrame и Series
- Создание DataFrame из словаря
- Создание Series с индексами

### 2. Чтение данных
- Чтение данных из CSV-файла

### 3. Анализ DataFrame
- Просмотр первых и последних строк (`head()`, `tail()`)
- Вывод информации о DataFrame (`info()`)

### 4. Индексирование
- Доступ к столбцам и строкам (`loc[]`, `iloc[]`)

### 5. Фильтрация данных
- Фильтрация строк на основе условий

### 6. Работа со столбцами
- Добавление нового столбца
- Переименование столбцов

### 7. Обработка отсутствующих данных
- Определение отсутствующих значений (`isnull()`)
- Заполнение пропущенных данных (`fillna()`)
- Удаление строк с пропущенными данными (`dropna()`)

### 8. Группировка и агрегация
- Группировка данных (`groupby()`)
- Вычисление суммы и среднего значения по группам

### 9. Объединение данных
- Объединение DataFrame с помощью `concat()`

### 10. Изменение формы данных
- Создание сводных таблиц (`pivot_table()`)
- Преобразование форматов с `melt()`
- Складывание и раскладывание данных (`stack()`, `unstack()`)

## Запуск кода

Файл можно запустить в Python:

```bash
python script.py
```

## Требования
- Python 3.x
- Pandas
- NumPy (при обработке отсутствующих данных)

## Автор
Разработано для демонстрации возможностей библиотеки Pandas в анализе и обработке данных.

