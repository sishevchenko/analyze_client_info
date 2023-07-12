import pandas as pd

from conf import EXCEL_FILE, DATASET

from sales import get_sales
from stores import get_store


def main():
    with pd.ExcelWriter(DATASET) as writer:
        get_store(EXCEL_FILE).to_excel(excel_writer=writer, sheet_name='store', index=False)
        get_sales(EXCEL_FILE).to_excel(excel_writer=writer, sheet_name='sales', index=False)



if __name__ == "__main__":
    try:
        print("start creating a dataset")
        main()
        print("dataset created as \"dataset.xlsx\" in main directory")
    except Exception as ex:
        print(ex)
