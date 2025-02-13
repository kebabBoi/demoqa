import time
from pages.alerts import Alerts

def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.equal_url()
    assert alert_page.btn_time_alert.exist()

    alert_page.btn_time_alert.click()
    time.sleep(6)

    alert_page.alert().accept()