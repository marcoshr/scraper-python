import time
from countdown import countdown
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = "info@marcoshr.com"
pwd = "apalabra224"

print("Abriendo Firefox...")
driver = webdriver.Firefox()

print("Entrando a Twitter...")
driver.get("https://twitter.com/?logged_out=1&lang=en")

print("Pulsando Log In...")
driver.find_element_by_css_selector('.js-nav.EdgeButton.EdgeButton--medium.EdgeButton--secondary.StaticLoggedOutHomePage-buttonLogin').click()

countdown()

print("Introduciendo usuario...")
driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus').send_keys(user)

print("Introduciendo contraseña...")
driver.find_element_by_css_selector('.js-password-field').send_keys(pwd)

print("Entrando a Twitter...")
driver.find_element_by_css_selector('.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()

print("Te has loggeado en tu perfil de Twitter.")
countdown(5)

print("Cerrando el navegador...")
countdown(5)
driver.close()