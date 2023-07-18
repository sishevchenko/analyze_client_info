import pandas as pd


def get_sales_frame(file):
    table = pd.ExcelFile(file)

    # Список фреймов для склейки
    data_frames = []

    for sheet in table.sheet_names:
        # Ищем нужные листы
        if 'sales' in sheet.lower():
            df = table.parse(sheet, header=None)

            # Удаляем пустые ячейки
            if df.isnull().values.any():
                df = df.dropna()
            
            # Удаляем лишние строки оглавления
            df = df[1:]

            df.columns = ['№ TT', 'НЕДЕЛЯ', 'КОЛ-ВО']

            data_frames.append(df)

    return pd.concat(data_frames, ignore_index=True)
