import time
from pages.webtables import Tables
from selenium.webdriver.common.keys import Keys

def test_check_tables(browser):
    webtables_page = Tables(browser)

    webtables_page.visit()
    assert not webtables_page.no_data.exist()

    while webtables_page.btn_delete.exist():
        webtables_page.btn_delete.click()
    time.sleep(2)
    assert webtables_page.no_data.exist()

def test_dialog_form(browser):
    webtables_page = Tables(browser)

    webtables_page.visit()
    assert webtables_page.btn_add.visible()
    webtables_page.btn_add.click()

    assert webtables_page.dialog_form.visible()

    webtables_page.btn_submit.click()
    assert webtables_page.dialog_form.visible()
    first_name = "Gadya"
    last_name = "Petrovich"
    email = "test@test.test"
    age = "10"
    salary = "9999"
    department = "Legal"
    webtables_page.first_name.send_keys(first_name)
    webtables_page.last_name.send_keys(last_name)
    webtables_page.email.send_keys(email)
    webtables_page.age.send_keys(age)
    webtables_page.salary.send_keys(salary)
    webtables_page.departament.send_keys(department)
    time.sleep(2)
    webtables_page.btn_submit.click()
    time.sleep(2)

    browser.set_window_size(1000, 1300)
    assert not webtables_page.dialog_form.exist()
    rows = webtables_page.rows.find_elements()
    assert len(rows) > 0

    last_filled_row = None
    for row in reversed(rows):  # Проход строки с конца
        if row.text.strip():  # Проверка, что строка не пустая
            last_filled_row = row
            break
    last_row_text = last_filled_row.text

    assert first_name in last_row_text
    assert last_name in last_row_text
    assert email in last_row_text
    assert age in last_row_text
    assert salary in last_row_text
    assert department in last_row_text

def test_two(browser):
    webtables_page = Tables(browser)

    webtables_page.visit()
    assert webtables_page.equal_url()

    webtables_page.rows_dropdown.scroll_to_element()
    webtables_page.rows_dropdown.click()
    webtables_page.rows_dropdown.send_keys(Keys.UP)
    webtables_page.rows_dropdown.click()
    time.sleep(2)

    assert webtables_page.rows.check_count_elements(count=5)

    assert not webtables_page.btn_next.click()
    assert webtables_page.btn_next.get_dom_attribute('disabled') == 'true'
    assert not webtables_page.btn_previous.click()
    assert webtables_page.btn_previous.get_dom_attribute('disabled') == 'true'

    for i in range(3):
        webtables_page.btn_add.click()

        assert webtables_page.dialog_form.visible()

        webtables_page.btn_submit.click()
        assert webtables_page.dialog_form.visible()
        first_name = "Gadya"
        last_name = "Petrovich"
        email = "test@test.test"
        age = "10"
        salary = "9999"
        department = "Legal"
        webtables_page.first_name.send_keys(first_name)
        webtables_page.last_name.send_keys(last_name)
        webtables_page.email.send_keys(email)
        webtables_page.age.send_keys(age)
        webtables_page.salary.send_keys(salary)
        webtables_page.departament.send_keys(department)
        time.sleep(2)
        webtables_page.btn_submit.click()
        time.sleep(2)

    assert webtables_page.pagination.get_text() == 'Page of 2'
    assert not webtables_page.btn_next.get_dom_attribute('disabled') == 'true'

    webtables_page.btn_next.click()
    assert webtables_page.pagination_text.get_dom_attribute('value') == '2'
    time.sleep(3)

    webtables_page.btn_previous.click()
    assert webtables_page.pagination_text.get_dom_attribute('value') == '1'
    time.sleep(3)