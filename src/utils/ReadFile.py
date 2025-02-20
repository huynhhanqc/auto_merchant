import logging
import pandas as pd


class ExcelUtils:
    @staticmethod
    def read_excel_data(file_path, sheet_name=None):
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            return df
        except Exception as e:
            logging.error(f"Error reading Excel file: {e}")
            return None
