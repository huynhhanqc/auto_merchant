import pytest
from src.data_base.database_connector import DatabaseConnector
from src.drivers.webdriver_factory import WebdriverFactory

@pytest.fixture
def db():
    db_connector = DatabaseConnector()
    db_connector.connect()
    yield db_connector
    db_connector.disconnect()

@pytest.mark.skip(reason="no reason")

class TestDataBase(WebdriverFactory):

    def test_db_connection(self,db: DatabaseConnector):
        assert db.connection.is_connected() == True, "Không thể kết nối tới cơ sở dữ liệu"

    def test_users_table(self,db: DatabaseConnector):
        result = db.fetch_one("SELECT * FROM user WHERE username = 'truonghan1506'")
        assert result is not None, "Không tìm thấy dữ liệu trong bảng users"
        assert result[1] == "truonghan1506", "Username không đúng"
        assert result[2] == "nguyen@example.com", "Email không đúng"

