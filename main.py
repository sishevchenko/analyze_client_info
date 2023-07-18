import pandas as pd

from conf import EXCEL_FILE, DATASET

from sales import get_sales_frame
from store import get_store_frame


def main():
    with pd.ExcelWriter(DATASET) as writer:
        get_store_frame(EXCEL_FILE).to_excel(excel_writer=writer, sheet_name='store', index=False)
        get_sales_frame(EXCEL_FILE).to_excel(excel_writer=writer, sheet_name='sales', index=False)


if __name__ == "__main__":
    try:
        print("start creating a dataset")
        main()
        print("dataset created as \"dataset.xlsx\" in main directory")
    except Exception as ex:
        print(ex)
