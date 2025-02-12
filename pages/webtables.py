from pages.base_page import BasePage
from components.components import WebElement

class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.rows = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]', 'xpath')
        self.table = WebElement(driver, '.rt-tbody')
        self.no_data = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-noData', 'css')
        self.btn_delete = WebElement(driver, '.rt-tr-group .action-buttons span[title="Delete"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.dialog_form = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.departament = WebElement(driver, '#department')
        self.name_in_row = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(3) > div > div:nth-child(1)')