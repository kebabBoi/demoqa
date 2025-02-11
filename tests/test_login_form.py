import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('papapa')
    form_page.user_email.send_keys('test@mail.cr')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('7777777777')
    form_page.hobbies.click_force()
    form_page.curr_address.send_keys('mama ya v dubayah :)')
    time.sleep(2)

    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

def test_state_and_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.state_dropdown.scroll_to_element()
    form_page.state_dropdown.click()
    form_page.btn_Haryana.click()
    time.sleep(2)

    form_page.city_dropdown.click()
    form_page.input_city.send_keys("Karnal")
    form_page.input_city.send_keys(Keys.ENTER)
    time.sleep(2)