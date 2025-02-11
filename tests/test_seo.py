from pages.demoqa import DemoQa

def test_check_title_demo(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert browser.title == 'DEMOQA'