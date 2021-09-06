import time
from countdown import countdown

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from credentials import user_endesa, pwd_endesa, user_aqualia, pwd_aqualia


print("Abriendo navegador...")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Firefox()

print("Entrando a Endesa...")
driver.get("https://www.endesaclientes.com/login.html?service=%2Foficina%2Fmis-facturas.html")

# ME FALLA EL CERRAR LAS COOKIES DE ENDESA, QUE NO CONSIGO PULSAR EN EL A[CLASS="CLOSE-BUTTON"]
# FECHA MIÉRCOLES 8 DE ABRIL DE 2020
print("Cerrando cookies...")
driver.find_element_by_xpath('a[href="#" class="close-button"]').click()
#driver.findElement(By.xpath('//a[href="#" class="close-button"]')).click();
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "close-button"))).click()

print("Introduciendo usuario...")   
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "alias"))).send_keys(user_endesa)
#driver.find_element_by_id('alias').send_keys(user_endesa)

print("Introduciendo contraseña...")
driver.find_element_by_id('password').send_keys(pwd_endesa)

print("Pulsando Log In...")
driver.find_element_by_id('loginButton').click()

countdown(2)





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