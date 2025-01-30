import pandas as pd



print('Создать фрейм данных')

data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

print('#' * 20)


print('Создание серии')

age_series = pd.Series([25, 30, 35], index=['Alice', 'Bob', 'Charlie'])
print(age_series)

print('#' * 20)


print('Чтение CSV-файлов')
df = pd.read_csv("people.csv")
print(df)

print('#' * 20)


print('Понимание и анализ фрейма данных')
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}

df = pd.DataFrame(data)

# View the first 3 rows of the DataFrame
print("First 3 rows using head():")
print(df.head(3))

# View the last 2 rows of the DataFrame
print("\nLast 2 rows using tail():")
print(df.tail(2))

# Get a concise summary of the DataFrame
print("\nDataFrame summary using info():")
df.info()

print('#' * 20)


print('Индексирование в Pandas')
data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]}
df = pd.DataFrame(data)
# Select a single column
age_column = df['Age']
print(age_column)

print('#' * 20)

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Using .loc[] to select rows by label
print('Использование .loc[] для выбора строк по метке')
row_by_label = df.loc[1]  # Selects the row with index label 1 (Bob's data)

# Using .iloc[] to select rows by position
print('Использование .iloc[] для выбора строк по позиции')
row_by_position = df.iloc[1]  # Selects the second row (Bob's data)

print("Row by label:\n", row_by_label)
print("Row by position:\n", row_by_position)


print('методы фильтрации на основе условий')

data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Filtering rows where Age is greater than 30
filtered_df = df[df['Age'] > 28]
print(filtered_df)

print('Работа со строками и столбцами в Pandas DataFrame')
print('1) Добавление нового столбца в DataFrame')

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})

# Adding a new column with a list of values
df['Salary'] = [50000, 60000, 70000]
print(df)

print('2) Переименование столбцов')

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Renaming columns
df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'}, inplace=True)
print(df)

print('3)  Переиндексация данных с помощью Pandas')

# Sample DataFrame
data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data)

# Reindex rows
new_index = [0, 1, 2, 3]
df_reindexed = df.reindex(new_index)
print("Reindexed Rows:\n", df_reindexed)

print('Обработка отсутствующих данных в Pandas')
print('1) Определение недостающих данных с помощью Pandas ')

import pandas as pd
import numpy as np
df = pd.DataFrame({'Col1': [1, 2, np.nan],'Col2': [3, np.nan, np.nan]})

# Check for missing values
print(df.isnull())

print('2) Заполнение пропущенных данных ')

import pandas as pd
import numpy as np
df = pd.DataFrame({'Col1': [1, 2, np.nan],'Col2': [3, np.nan, np.nan]})
df.fillna(0)
print(df)

print('3)  Удаление отсутствующих данных с помощью Pandas')

import pandas as pd
data = {'Name': ['Alice', 'Bob', None], 'Age': [25, None, 35]}
df = pd.DataFrame(data)

# Drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

print('Агрегация и группировка с помощью Pandas')

import pandas as pd
data = {'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Group data by 'Category' and calculate the sum
grouped_sum = df.groupby('Category').sum()
print("Sum:\n", grouped_sum)

# Compute the mean for each group
grouped_mean = df.groupby('Category')['Value'].mean()
print("\nMean:\n", grouped_mean)

# Aggregate using multiple functions
grouped_agg = df.groupby('Category').agg(['sum', 'mean'])
print("\nAggregated:\n", grouped_agg)



print('    2. Объединение данных ')
import pandas as pd
data = {'Name': ['Alice', 'Charlie', 'Edward', 'Grace'],'Years_Experience': [2, 3, 4, 6],'Role': ['Manager', 'Analyst', 'Developer', 'HR']}
df = pd.DataFrame(data)

# New DataFrame to concatenate
new_data = {'Name': ['John', 'Lily'],'Years_Experience': [5, 3],'Role': ['Designer', 'Developer']}
new_df = pd.DataFrame(new_data)

# Concatenate the original and new DataFrames along rows (axis=0)
concatenated_df = pd.concat([df, new_df], axis=0, ignore_index=True)

print("Concatenated DataFrame:\n", concatenated_df)


print('Изменение формы данных в Pandas')
print('    1. Сводные таблицы в Pandas')

import pandas as pd
data = {'Date': ['2024-10-01', '2024-10-01', '2024-10-02', '2024-10-02'],'Category': ['A', 'B', 'A', 'B'],'Values': [10, 20, 15, 25]}
df = pd.DataFrame(data)

pivot_table = df.pivot_table(values='Values', index='Date', columns='Category', aggfunc='sum')
print(pivot_table)

print('    2. Плавление и расплавление')

import pandas as pd
data = {'Date': ['2024-10-01', '2024-10-01', '2024-10-02', '2024-10-02'],'Category': [10, None, 15, None],'Category_B': [None, 20, None, 25]}
df = pd.DataFrame(data)

# Melt data from wide to long format
melt_df = df.melt(id_vars='Date', var_name='Category', value_name='Values')
print(melt_df)

print('    3. Складывание и раскладывание с помощью Pandas')

import pandas as pd
data = {
    ('Sales', 'Q1'): [100, 150],
    ('Sales', 'Q2'): [200, 250],
    ('Expenses', 'Q1'): [50, 70],
    ('Expenses', 'Q2'): [80, 90]
}

index = ['Product_A', 'Product_B']
df = pd.DataFrame(data, index=index)
print(df)

stacked_df = df.stack() # Columns → Rows
print(stacked_df)

unstacked_df = stacked_df.unstack() # Rows → Columns
print(unstacked_df)



