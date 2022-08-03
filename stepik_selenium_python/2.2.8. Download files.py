# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome(executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)

First_name = driver.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
First_name.send_keys('Olga')

Last_name = driver.find_element(By.NAME, 'lastname')
Last_name.send_keys('Vashkevich')

Email = driver.find_element(By.XPATH, "//input[@name='email']")
Email.send_keys('1@23-OV.com')

# файл в той же директории
current_dir = os.path.abspath(os.path.dirname('C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\stepik_selenium_python\\'))
# current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = driver.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

# файл создаю в пайтоне
# with open('test1.txt', 'w') as file:
#    file.write('test1 for mls 228')
  # content = file.write("automationbypython")  # create test.txt file

# path = os.getcwd() + '/' + file.name
# path = os.getcwd() + '\\' + test1.txt


# submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(10)
driver.close()

