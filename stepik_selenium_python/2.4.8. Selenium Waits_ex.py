# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import def_for_ex as ex

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)

# driver.implicitly_wait(12)

# price_element = driver.find_element(By.ID, 'price')
# WebDriverWait(browser, "время ожидания работы счетчика")
# .until(EC.text_to_be_present_in_element((By.ID, "ИД текста"), "текст для сравнения"))   // Задаем счетчик ожидания
# btn = browser.find_element_by_id("book") // Объявляем кнопку
# btn.click() // И прокликиваем
price_element = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

driver.find_element(By.ID, 'book').click()

# Два способа проскролить:1. Опускаем экран 2. Задаем элемент и скролим до него
# driver.execute_script("window.scrollBy(0, 450);")
solve = driver.find_element(By.ID, "solve")
driver.execute_script("return arguments[0].scrollIntoView(true);", solve)

x_element = driver.find_element(By.ID, 'input_value')
x = int(x_element.text)

def calc(z):
    return str(math.log(abs(12 * math.sin(int(z)))))

# y = ex.calc(x)
y = calc(x)
y_answer = driver.find_element(By.ID, 'answer')
y_answer.send_keys(y)

solve.click()

# Копирование числа из алерта в буфер обмена
alert = driver.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

time.sleep(10)
driver.close()