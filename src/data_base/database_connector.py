import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Kết nối MySQL thành công")
            else:
                raise Exception("Kết nối không thành công")
        except Error as e:
            print(f"Lỗi kết nối: {e}")
            raise  

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            print("Đã ngắt kết nối MySQL")
        else:
            print("Không có kết nối để đóng")

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            raise Exception("Chưa kết nối tới cơ sở dữ liệu")
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor.fetchall()
        except Error as e:
            print(f"Lỗi truy vấn: {e}")
            raise

    def fetch_one(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            raise Exception("Chưa kết nối tới cơ sở dữ liệu")
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Error as e:
            print(f"Lỗi truy vấn: {e}")
            raise