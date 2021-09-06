import time
from countdown import countdown
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

countdown(1)

print("Introduciendo usuario...")
driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus').send_keys(user)

print("Introduciendo contraseña...")
driver.find_element_by_css_selector('.js-password-field').send_keys(pwd)

print("Entrando a Twitter...")
driver.find_element_by_css_selector('.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()

print("Te has loggeado en tu perfil de Twitter.")
countdown(1)

driver.execute_script("window.scrollTo(0, 150)")

"""
print("Entrando al perfil " + perfil + "...")
driver.get("https://twitter.com/" + perfil)

#countdown(1)
print("Pulso en seguidores")
driver.find_element_by_css_selector('.ProfileNav-list li:nth-child(3) a').click()

countdown(1)
print("Pulso en botón de seguir")
follow_buttons = driver.find_elements_by_css_selector('.EdgeButton.EdgeButton--secondary.EdgeButton--small.button-text.follow-text')

count = 1
for follow_button in follow_buttons:
    if count == 50:
        break
    follow_button.click()
    driver.execute_script("window.scrollTo(0, 150)") 
    countdown()
    print(str(count) + " seguido.")
    count += 1

# element could not be scrolled into view
# cuidado con los limites para seguir
"""

print("Fin.")
countdown(10)
print("Cerrando el navegador...")
countdown(5)
driver.close()