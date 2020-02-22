# 2.4 Настройка ожиданий. Step 8. Задание: ждем нужный текст на странице

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/explicit_wait2.html"
timeout = 12
target_price = "$100"

# The 'with' statement clarifies code
# that previously would use try...finally blocks
# to ensure that clean-up code is executed.
# https://docs.python.org/2.5/whatsnew/pep-343.html

with webdriver.Chrome() as browser:
    # setting a wait
    wait = WebDriverWait(browser, timeout)

    # "buy" at the target price
    browser.get(link)
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), target_price))
    browser.find_element_by_css_selector("#book").click()

    # get the code
    x = int(browser.find_element_by_css_selector("#input_value").text)
    answer = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(answer)
    browser.find_element_by_css_selector("#solve").click()
    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()

print(text)
