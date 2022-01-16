AMAZON_URL = "https://www.amazon.com"
SEARCH_FIELD_ID = "twotabsearchtextbox"
SEARCH_FOR = "fidget spinner"
SEARCH_SUBMIT_ID = "nav-search-submit-button"
SORT_ELEMENT_ID = 's-result-sort-select'
SORT_BY_TEXT = "Avg. Customer Review"
ADD_TO_CART_BUTTON_ID = "add-to-cart-button"
CARD_ELEMENT_ID = "nav-cart"
CARD_PRODUCTS_SUBTOTAL_ID = "sc-subtotal-label-activecart"
PRODUCTS_IN_CARD_CLASS_NAME = "sc-list-item-content"
DELETE_SECOND_PRODUCT_FROM_CARD_PATH = "/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[4]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input"
CARD_TOTAL_AMOUNT_ID = "sc-subtotal-amount-activecart"
CARD_TOTAL_AMOUNT = " $12.99"


def product_path_by_number(product_number: int) -> str:
    """
    Returns product xpath
    :param product_number: int use in range 1-48
    :return: xpath
    """
    return f"//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[{product_number}]"

