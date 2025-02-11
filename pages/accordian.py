from  pages.base_page import BasePage
from components.components import WebElement

class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.text_card = WebElement(driver, '#section1Content > p')
        self.text_card_two = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.text_card_twotwo = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.text_card_three = WebElement(driver, '#section3Content > p')
        self.title_card = WebElement(driver, '#section1Heading')