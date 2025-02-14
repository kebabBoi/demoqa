from pages.demoqa import DemoQa
from pages.radio_button import Radio
import pytest

@pytest.mark.skip
def test_decor_1(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert demoqa_page.card.check_count_elements(count=6)

    for element in demoqa_page.card.find_elements():
        assert element.text != ''

@pytest.mark.skipif(True, reason="так надо")
def test_decor_2(browser):
    radio_page = Radio(browser)

    radio_page.visit()
    radio_page.yes.click_force()
    assert radio_page.text.get_text() == 'You have selected Yes'

    radio_page.impressive.click_force()
    assert radio_page.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio_page.no.get_dom_attribute('class')