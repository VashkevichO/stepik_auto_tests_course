# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = "http://SunInJuly.github.io/execute_script.html"
driver.get(link)

x_element = driver.find_element(By.ID, 'input_value')
x = int(x_element.text)
# print(x)


def calc(z):
    return str(math.log(abs(12 * math.sin(int(z)))))


# print(calc(x))
y = calc(x)
y_answer = driver.find_element(By.ID, 'answer')
y_answer.send_keys(y)

# button = driver.find_element_by_tag_name("button")
# driver.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

# button = browser.find_element(By.TAG_NAME, "button")
# button.click()

driver.execute_script("window.scrollBy(0, 150);")

robotCheckbox = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

robotsRule = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

submit = driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(10)
driver.close()