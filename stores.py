import pandas as pd


def get_store(file):
    table = pd.ExcelFile(file)
    
    df = table.parse(table.sheet_names[1])

    # Удаляем лишний столбец
    df = df.drop("БЛК", axis=1) 

    # Собираем необходимые нам колонки в список
    new_columns = list(df.columns)
    new_columns.pop(1)

    # Создаем копии слайсов исходного фрейма
    df_upper = df.loc[:148, new_columns].copy()
    df_lower = df.loc[149:, df.columns[:-1]].copy()
    
    # Переименовываем колонки нижней части фрейма
    df_lower.columns = new_columns

    # Склеиваем фрейм и заменяем названия колонок
    df = pd.concat([df_upper, df_lower], axis=0, ignore_index=True)

    df.columns = ["№ ТТ", "ГОРОД", "РЕГИОН", "ШИР.", "ДОЛ.", "ДАТА ОТКР", "ДАТА ЗАКР."]

    # Удаляем лишнюю строку названия колонок
    df = df.drop(0)

    return df
