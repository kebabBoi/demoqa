import time
from pages.text_box import TextBox

def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    full_name = 'Vaho Brooklyn'
    curr_address = 'Мой адрес не дом и не улица'
    text_box_page.full_name.send_keys(full_name)
    text_box_page.curr_address.send_keys(curr_address)
    text_box_page.btn_submit.click()
    time.sleep(2)

    output_full_name = text_box_page.output_full_name.get_text()
    output_curr_address = text_box_page.output_curr_address.get_text()

    assert full_name in output_full_name
    assert curr_address in output_curr_address