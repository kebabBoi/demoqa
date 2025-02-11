from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text_element(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert demo_qa_page.text_footer.get_text() == expected_text

    demo_qa_page.button_elements.click()
    expected_text_two = 'Please select an item from left to start practice.'
    assert demo_qa_page.text_center.get_text() == expected_text_two

def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()