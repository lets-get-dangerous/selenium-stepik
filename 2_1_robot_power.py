# 2.1 Основные методы Selenium. Step 5. Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

# The 'with' statement clarifies code
# that previously would use try...finally blocks
# to ensure that clean-up code is executed.
# https://docs.python.org/2.5/whatsnew/pep-343.html

with webdriver.Chrome() as browser:
  # load page
  browser.get(link)

  # fill out the robo-captcha
  x = int(browser.find_element_by_id("input_value").text)
  answer = calc(x)
  browser.find_element_by_css_selector("#answer").send_keys(answer)

  # submit "i'm the robot" and "robot rule!"
  browser.find_element_by_css_selector("#robotsRule").click()
  browser.find_element_by_css_selector("#robotCheckbox").click()
  browser.find_element_by_xpath("//button[@type='submit']").click()

  # get key
  alert = browser.switch_to.alert
  text  = alert.text
  alert.accept()

print(text)

