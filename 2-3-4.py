from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button1 = browser.find_element_by_xpath("//button[@type='submit']")
button1.click()

time.sleep(3)

confirm = browser.switch_to.alert
confirm.accept()


x_element = browser.find_element_by_xpath("//span[@id='input_value'] ")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_xpath("//input[@id='answer']")
input1.send_keys(y)

button2 = browser.find_element_by_xpath("//button[@type='submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()

time.sleep(15)