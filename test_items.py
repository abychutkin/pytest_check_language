import time


def test_guest_should_see_purchase_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    browser.find_element_by_css_selector('button.btn-add-to-basket')
