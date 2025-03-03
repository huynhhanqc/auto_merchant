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

    def test_work_schedule_table(self,db: DatabaseConnector):
        query = "SELECT * FROM vendor_staff_schedule WHERE id = '803'"
        result = db.fetch_all(query)
        assert result is not None, "Không thể thực hiện truy vấn"
        assert len(result) > 0, "Không có dữ liệu trong bảng vendor_staff_schedule"
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>{result}")
    
        

