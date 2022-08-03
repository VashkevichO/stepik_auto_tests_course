# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

driver = webdriver.Chrome(executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)

button1 = driver.find_element(By.TAG_NAME, 'button').click()

confirm = driver.switch_to.alert
confirm.accept()

x_element = driver.find_element(By.ID, 'input_value')
x = int(x_element.text)

def calc(z):
    return str(math.log(abs(12 * math.sin(int(z)))))

y = calc(x)
y_answer = driver.find_element(By.ID, 'answer')
y_answer.send_keys(y)

button2 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(10)
driver.close()