import time
from pages.form_page import FormPage

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('papapa')
    form_page.user_email.send_keys('test@mail.cr')
    form_page.male_radio_btn.click()
    form_page.user_number.send_keys('7777777777')
    time.sleep(2)

    form_page.btn_submit.click()
    time.sleep(2)