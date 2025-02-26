import openpyxl
import random

class ExcelReader:
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = openpyxl.load_workbook(self.file_path)
        self.sheet = self.workbook[self.sheet_name]

    def get_random_values(self, column_letter, num_values):
        values = [cell.value for cell in self.sheet[column_letter] if cell.value is not None]
        return random.sample(values, min(num_values, len(values)))