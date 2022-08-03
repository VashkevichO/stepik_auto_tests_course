# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome(executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = "http://suninjuly.github.io/get_attribute.html"
driver.get(link)
#time.sleep(10)

x_element = driver.find_element(By.CSS_SELECTOR, '[id="treasure"]')
x = x_element.get_attribute("valuex")
# valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')
#print(x)
y = calc(x)
# print(y)

y_answer = driver.find_element(By.CSS_SELECTOR, '[id="answer"]')
y_answer.send_keys(y)

robotCheckbox = driver.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]').click()

radiobutton = driver.find_element(By.CSS_SELECTOR, '[id="robotsRule"]').click()

button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()

# # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
# for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
#   browser.find_element_by_css_selector(selector).click()

time.sleep(10)
driver.close()


