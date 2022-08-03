# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(
    executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'
driver.get(link)
# driver.get(link2)

num1_element = driver.find_element(By.ID, 'num1')
num1 = int(num1_element.text)
print(num1)

num2_element = driver.find_element(By.CSS_SELECTOR, '[id="num2"]')
num2: int = int(num2_element.text)
print(num2)

def sum(x, y):
    return str(x + y)
# print(sum(num1, num2))

select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(sum(num1, num2))

button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()

# time.sleep(1)
# driver.close()