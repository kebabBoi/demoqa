from pages.links import Links
from pages.demoqa import DemoQa
import time

def test_window_tab(browser):
    links_page = Links(browser)
    demoqa_page = DemoQa(browser)

    links_page.visit()
    assert links_page.equal_url()
    assert links_page.link_home.exist()
    assert links_page.link_home.get_text() == 'Home'
    assert links_page.link_home.get_dom_attribute('href') == 'https://demoqa.com'

    assert len(browser.window_handles) == 1
    links_page.link_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    assert demoqa_page.equal_url()