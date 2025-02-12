import time
from pages.koup import Koup
from pages.koup_add import KoupAdd

def test_btn_add(browser):
    koup_page = Koup(browser)
    koupadd_page = KoupAdd(browser)

    koup_page.visit()
    assert koup_page.link.get_text() == 'Add/Remove Elements'
    koup_page.link.click()
    assert koupadd_page.equal_url()

    assert koupadd_page.btn_add.get_text() == 'Add Element'
    assert koupadd_page.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        koupadd_page.btn_add.click()
    time.sleep(2)

    assert koupadd_page.btn_delete.check_count_elements(count=4)

    #проверка для всех элементов
    for element in koupadd_page.btn_delete.find_elements():
        assert  element.text == 'Delete'

    while koupadd_page.btn_delete.exist():
        koupadd_page.btn_delete.click()

    assert not koupadd_page.btn_delete.exist()