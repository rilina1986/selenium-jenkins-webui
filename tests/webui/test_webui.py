import logging
import time

from selenium.webdriver import Chrome

from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement
from tests.webui.test_data import (
    SEARCH_FOR,
    AMAZON_URL,
    SEARCH_SUBMIT_ID,
    SEARCH_FIELD_ID,
    SORT_BY_TEXT,
    SORT_ELEMENT_ID,
    product_path_by_number,
    ADD_TO_CART_BUTTON_ID,
    CARD_ELEMENT_ID,
    PRODUCTS_IN_CARD_CLASS_NAME,
    CARD_TOTAL_AMOUNT,
    DELETE_SECOND_PRODUCT_FROM_CARD_PATH,
    CARD_TOTAL_AMOUNT_ID,
)
from selenium.webdriver.support.ui import Select


LOG = logging.getLogger(__name__)


def add_product_to_card(
    chrome_driver,
    element_finder,
    element_actions,
    product_number: int,
    back_to_products_page=True,
):
    product = element_finder.by_xpath(product_path_by_number(product_number))
    element_actions.click(product)
    element_actions.click(element_finder.by_id(ADD_TO_CART_BUTTON_ID))
    if back_to_products_page:
        chrome_driver.back()
        chrome_driver.back()


def products_number_in_card(element_finder) -> int:
    products_in_card = element_finder.list_by_class_name(PRODUCTS_IN_CARD_CLASS_NAME)
    number = len(products_in_card)
    LOG.info("PRODUCTS IN CARD: %s", number)
    return number


def test_web_table(
    chrome_driver: Chrome,
    element_finder: FindElement,
    element_actions: ElementActions,
):
    chrome_driver.get(AMAZON_URL)
    search_element = element_finder.by_id(SEARCH_FIELD_ID)
    LOG.info("Search element %s", search_element)
    element_actions.input_text(search_element, SEARCH_FOR)
    search_submit = element_finder.by_id(SEARCH_SUBMIT_ID)
    element_actions.click(search_submit)

    select = Select(element_finder.by_id(SORT_ELEMENT_ID))
    select.select_by_visible_text(SORT_BY_TEXT)
    # time.sleep(2)

    add_product_to_card(chrome_driver, element_finder, element_actions, 4)
    add_product_to_card(chrome_driver, element_finder, element_actions, 5, False)
    element_actions.click(element_finder.by_id(CARD_ELEMENT_ID))

    assert products_number_in_card(element_finder) is 2
    delete_element = element_finder.by_xpath(DELETE_SECOND_PRODUCT_FROM_CARD_PATH)
    element_actions.click(delete_element)
    time.sleep(2)
    assert (
        products_number_in_card(element_finder) is 1
    ), "PRODUCT NUMBER IN CARD IS NOT 1"
    amount = str(element_finder.by_id(CARD_TOTAL_AMOUNT_ID).text)
    LOG.info("CARD TOTAL AMOUNT: %s", amount)
    assert amount == CARD_TOTAL_AMOUNT, "CARD TOTAL AMOUNT IS NOT $12.99"
