from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class EvaMainPage(BasePage):
    URL = 'https://eva.ua/ua/'
    CHECKOUT_URL = 'https://eva.ua/ua/checkout/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(EvaMainPage.URL)

    def try_add_item_to_cart(self):
        btn_elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart")))
        btn_elem.click()

    def check_add_to_card_success_message(self):
        is_start_correct = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "m-microcart-notifications-item--success"), 'Ви додали '))
        is_end_correct = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "m-microcart-notifications-item--success"), ' до Вашого кошика покупок.'))
        return is_start_correct and is_end_correct

    def try_change_quantity(self):
        listbox_elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.m-microcart-item__wrap-price > div.m-microcart-item__qty > div")))
        listbox_elem.click()
        li_elems = listbox_elem.find_elements(By.CSS_SELECTOR, "li")
        index = random.randint(1, len(li_elems) - 1)
        li_elems[index].click()

    def check_change_qnt_success_message(self):
        is_message_correct = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "m-microcart-notifications-item--success"), 'Кількість товару оновлено!'))
        return is_message_correct
    
    def add_always_needed(self):
        btn_elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__container .product__actions")))
        btn_elem.click()

    def check_add_always_needed_success_message(self):
        is_start_correct = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "m-microcart-notifications-item--success"), 'Ви додали '))
        is_end_correct = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "m-microcart-notifications-item--success"), ' до Вашого кошика покупок.'))
        return is_start_correct and is_end_correct
    
    def delete_item_from_cart(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "m-microcart-item__action-delete")))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "m-microcart-item__action-delete")))
        btn_elem = self.driver.find_elements(By.CLASS_NAME, "m-microcart-item__action-delete")
        btn_elem[-1].click()

    def get_current_cart_amound(self):
        self.wait_until_spinner_off()
        header = self.driver.find_element(By.CSS_SELECTOR, ".sf-heading__title.sf-heading__title--h2")
        return int(header.text.split(" ") [-1])

    def wait_until_spinner_off(self):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.CLASS_NAME, "m-modal-microcart__spinner")))
        
    def make_purchase(self):        
        btn_elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__container .m-modal-microcart-totals__button")))
        btn_elem.click()

    def check_checkout_url(self):
        return WebDriverWait(self.driver, 15).until(EC.url_changes(EvaMainPage.CHECKOUT_URL))
        