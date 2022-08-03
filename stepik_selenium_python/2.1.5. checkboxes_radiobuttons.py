import math
from selenium import webdriver
import time
# класс By, который содержит все возможные локаторы.
from selenium.webdriver.common.by import By

#3. Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#1. Открыть страницу http://suninjuly.github.io/math.html

#Настраиваем открытие страницы через хром
driver = webdriver.Chrome(executable_path="C:\\Users\\Timepad-admin\\PycharmProjects\\Selenium\\Offen_use\\chromedriver.exe")

# запросы (try and finaly - обязательное исполнение, expeption - не обяз, обычно ошибки показывает
# try:
link = "http://suninjuly.github.io/math.html"
driver.get(link)
time.sleep(4) #чтобы сразу страница не закрывалась
#    driver.get(url=url)
    #time.sleep(8) #чтобы сразу страница не закрывалась
    # link = "http://suninjuly.github.io/math.html"
  #  browser = webdriver.Chrome()
  #  browser.get(link)
#  time.sleep(4) #чтобы сразу страница не закрывалась
# закрытие лишних вкладок
# finally:
#     driver.close()  #тек страницу закрываем
 #   driver.quit()   #все стр закрываем

# 2. Считать значение для переменной x.

x_element = driver.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение".
x = int(x_element.text)
#print(x)
y = calc(x)



#3. Посчитать математическую функцию от x
#    import math

# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))

#4. Ввести ответ в текстовое поле.
y_answer = driver.find_element(By.CSS_SELECTOR, '[id="answer"]')
y_answer.send_keys(y)
#5. Отметить checkbox "I'm the robot".
robotCheckbox = driver.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
# robotCheckbox.click()
#6. Выбрать radiobutton "Robots rule!".
radiobutton = driver.find_element(By.CSS_SELECTOR, '[Id="robotsRule"]').click()
# radiobutton.click()
#7. Нажать на кнопку Submit.
button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
# button.click()

