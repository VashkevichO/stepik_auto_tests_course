# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

# говорим WebDriver искать каждый элемент в течение 2 секунд
driver.implicitly_wait(2)

driver.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()

# Имя текущей вкладки
# first_window = driver.window_handles[0]
# print(first_window)
# Имя новой вкладки
second_window = driver.window_handles[1]
# print(first_window)
# переключиться на новое окно
driver.switch_to.window(second_window)

x_element = driver.find_element(By.ID, 'input_value')
x = int(x_element.text)

def calc(z):
    return str(math.log(abs(12 * math.sin(int(z)))))

y = calc(x)
y_answer = driver.find_element(By.ID, 'answer')
y_answer.send_keys(y)

# button2 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(10)
driver.close()