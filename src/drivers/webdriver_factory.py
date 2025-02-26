import pytest

@pytest.mark.usefixtures("setup_teardown")
# @pytest.mark.usefixtures("chrome_driver_headless")
# @pytest.mark.usefixtures("firefox_driver_headless")
# @pytest.mark.usefixtures("edge_driver_headless")
class WebdriverFactory:
    pass   