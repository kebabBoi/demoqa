import time
from pages.accordian import Accordian

def test_visible_accordian(browser):
     accordian_page = Accordian(browser)

     accordian_page.visit()
     assert accordian_page.text_card.visible()

     accordian_page.title_card.click()
     time.sleep(2)
     assert not accordian_page.text_card.visible()

def test_visible_accordion_default(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert not accordian_page.text_card_two.visible()
    assert not accordian_page.text_card_twotwo.visible()
    assert not accordian_page.text_card_three.visible()