import time
from countdown import countdown
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user = "info@marcoshr.com"
pwd = "apalabra224"

perfil = "perezreverte"

print("Abriendo navegador...")
driver = webdriver.Firefox()
#driver = webdriver.Chrome()

print("Entrando a Twitter...")
driver.get("https://twitter.com/?logged_out=1&lang=en")

print("Pulsando Log In...")
driver.find_element_by_css_selector('.js-nav.EdgeButton.EdgeButton--medium.EdgeButton--secondary.StaticLoggedOutHomePage-buttonLogin').click()

countdown(2)

print("Introduciendo usuario...")
driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus').send_keys(user)

print("Introduciendo contraseña...")
driver.find_element_by_css_selector('.js-password-field').send_keys(pwd)

print("Entrando a Twitter...")
driver.find_element_by_css_selector('.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()

print("Te has loggeado en tu perfil de Twitter.")
countdown(1)

print("Entrando al perfil " + perfil + "...")
driver.get("https://twitter.com/" + perfil)

countdown()
#driver.find_element_by_css_selector('.Banner-actions button').click()

countdown(1)
print("Pulso en seguidores")
driver.find_element_by_css_selector('.ProfileNav-list li:nth-child(3) a').click()


countdown(1)
print("Pulso en botón de seguir")


driver.find_element_by_css_selector('.EdgeButton.EdgeButton--secondary.EdgeButton--small.button-text.follow-text')

count = 1
while True:
    if count == 50:
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = driver.find_element_by_css_selector('.EdgeButton.EdgeButton--secondary.EdgeButton--small.button-text.follow-text')
    button.click()
    print(str(count) + " seguido.")
    count += 1

print("Fin.")
countdown(10)
print("Cerrando el navegador...")
countdown(5)
driver.close()