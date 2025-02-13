import time
import pytest
from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)

    # if not modal_dialogs_page.is_page_accessible():
    #     pytest.skip()

    modal_dialogs_page.visit()
    assert modal_dialogs_page.equal_url()
    assert modal_dialogs_page.btn_small_modal.exist()
    assert modal_dialogs_page.btn_large_modal.exist()

    modal_dialogs_page.btn_small_modal.click()
    assert modal_dialogs_page.modal.exist()
    modal_dialogs_page.close_modal.click()
    time.sleep(2)

    modal_dialogs_page.btn_large_modal.click()
    assert modal_dialogs_page.modal.exist()
    modal_dialogs_page.close_modal.click()
    time.sleep(2)

    assert True