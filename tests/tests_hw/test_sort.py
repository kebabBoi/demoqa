from pages.webtables import Tables

def test_sort(browser):
    webtables_page = Tables(browser)

    webtables_page.visit()
    assert webtables_page.equal_url()

    for webtables_page.headers in webtables_page.headers.find_elements():
        initial_class = webtables_page.headers.get_dom_attribute('class')
        webtables_page.headers.click()
        assert webtables_page.headers.get_dom_attribute('class') != initial_class